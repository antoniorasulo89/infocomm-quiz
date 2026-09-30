"""Compile editorial questions. The copyrighted textbook is never copied to public/."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
modules = []
topic = ''
for line in (ROOT / 'content/bank.txt').read_text(encoding='utf-8').splitlines():
    if not line or line.startswith('#'): continue
    if line.startswith('@'):
        mid, title, description, first, last = line[1:].split('|')
        module = dict(id=mid, title=title, description=description, book_pages=[int(first),int(last)],questions=[])
        modules.append(module)
    elif line.startswith('%'): topic=line[1:]
    else:
        prompt, correct, wrong, page, explanation, statement, truth = line.split('|')
        for kind, q, options, answer in [('multiple',prompt,[correct]+wrong.split('~'),0),('truefalse',statement,['Vero','Falso'],0 if truth=='V' else 1)]:
            page=int(page)
            module['questions'].append(dict(id=f"{module['id']}-q{len(module['questions'])+1:02d}",q=q,options=options,answer=answer,explanation=explanation,topic=topic,difficulty='base' if kind=='truefalse' else 'intermedia',source=f'InfoComm, ed. 2021 · p. {page} (PDF p. {page+16})',bookPage=page,pdfPage=page+16,type=kind))

# Existing questions revised against the chapter contents. Each line is page | explanation.
NOTES = {
'a6': '''245|L’AOO raggruppa uffici e servizi che condividono criteri di gestione documentale e protocollo.
256|La fattura elettronica contiene dati strutturati in XML; il sistema di interscambio ne gestisce il transito.
260|Il modello precompilato contiene informazioni già disponibili, che il contribuente deve verificare e può integrare.
266|Il MePA è un mercato elettronico per gli acquisti della Pubblica Amministrazione.
280|PagoPA permette di effettuare pagamenti verso gli enti aderenti con procedure e ricevute digitali.
275|SPID permette di identificarsi per accedere a servizi online aderenti, usando un’identità digitale.
265|L’e-procurement riguarda l’approvvigionamento tramite strumenti e piattaforme elettroniche.
256|XML organizza i dati della fattura in una struttura leggibile ed elaborabile dai sistemi informatici.
280|La ricevuta e gli identificativi del pagamento aiutano a documentare l’operazione effettuata.
275|L’identità digitale permette di accedere a più servizi aderenti senza creare un’identità distinta per ciascuno.
244|Il protocollo registra i documenti secondo le procedure dell’ente, in entrata e in uscita.
244|La registrazione di protocollo associa al documento informazioni identificative, come numero e data.
247|Il fascicolo collega documenti relativi a una pratica o a un procedimento, rendendoli reperibili insieme.
243|Il documento informatico rappresenta in forma digitale atti, fatti o dati rilevanti; la sua efficacia dipende dai requisiti applicabili.
248|L’accettazione del documento richiede controlli e registrazioni previsti nel flusso documentale.
259|La conservazione è un processo organizzato per mantenere documenti accessibili, integri e utilizzabili nel tempo.
247|Il titolario è uno schema di classificazione: organizza i documenti secondo le funzioni dell’ente.
279|L’anagrafe nazionale centralizza i dati anagrafici della popolazione residente.
260|La precompilazione usa dati già disponibili all’amministrazione, ma non elimina la verifica da parte dell’interessato.
260|Il 730 è un modello di dichiarazione dei redditi rivolto, tra gli altri, a lavoratori dipendenti e pensionati.
265|L’approvvigionamento elettronico porta online fasi del processo di acquisto di beni e servizi.
267|Gli strumenti di acquisto permettono di scegliere modalità adatte alle esigenze di approvvigionamento della PA.
258|Il codice destinatario permette il recapito attraverso il sistema di interscambio; il contesto PA ha specifiche proprie.
256|Una semplice immagine o scansione non contiene la struttura XML richiesta al file fattura.
249|Un workflow descrive il percorso del documento tra attività, soggetti e verifiche.
268|L’abilitazione permette alle imprese di operare nel mercato elettronico secondo le categorie e i requisiti previsti.
276|Il secondo livello SPID aggiunge un fattore di verifica alla password, ad esempio una credenziale temporanea.
275|L’identificazione digitale permette a un servizio di riconoscere l’utente che chiede accesso.
281|IO offre un punto di accesso da smartphone a comunicazioni e servizi degli enti aderenti.
246|Il responsabile della gestione documentale coordina le attività e le regole di gestione dei documenti.
277|L’accesso con SPID richiede il riconoscimento tramite il gestore dell’identità e il livello previsto dal servizio.
244|Il protocollo riguarda anche i documenti in entrata: non soltanto quelli spediti dall’ente.
259|La conservazione richiede procedure e responsabilità; non coincide con il semplice salvataggio di un file in una cartella.
260|I dati del 730 precompilato possono richiedere verifica, correzione e integrazione.
258|Lo SDI svolge controlli e recapita le fatture secondo il flusso previsto.
280|Il pagamento digitale produce elementi utili a identificare e documentare l’operazione.
276|I livelli di sicurezza SPID prevedono requisiti di autenticazione differenti.
281|IO riunisce servizi e comunicazioni della Pubblica Amministrazione aderente.
247|Classificare i documenti con criteri comuni ne facilita organizzazione e recupero.
258|Le informazioni di recapito indirizzano la fattura verso il destinatario nel sistema di interscambio.''',
'b1': '''294|HTML descrive la struttura e il significato degli elementi della pagina; lo stile è affidato ai CSS.
300|Il tag p identifica un paragrafo. In una pagina moderna l’allineamento si imposta tramite CSS.
314|I CSS separano le regole di presentazione dalla struttura HTML e ne facilitano il riuso.
320|Una classe si applica tramite l’attributo class e può essere assegnata a più elementi.
326|HTML5 comprende elementi semantici e tipi di input per dati come email e date.
292|Usabilità e accessibilità favoriscono comprensione e fruizione, anche con tecnologie assistive.
334|Un CMS gestisce contenuti e pubblicazione attraverso strumenti dedicati, senza riscrivere manualmente ogni pagina.
314|Separare struttura e presentazione facilita aggiornamenti e coerenza tra pagine.
300|La proprietà CSS text-align permette di scegliere l’allineamento del testo nel contenitore.
292|Etichette chiare e navigazione comprensibile aiutano gli utenti a orientarsi.
300|Il tag p delimita un paragrafo di testo.
299|I titoli da h1 a h6 esprimono livelli gerarchici, non soltanto differenze di dimensione.
303|ul identifica una lista non ordinata; ol identifica una lista ordinata.
308|Le tabelle organizzano dati in righe e celle, utili quando esistono relazioni tabellari.
314|div è un contenitore generico per raggruppare elementi e applicare regole di stile.
314|span è un contenitore generico in linea, usato anche per applicare stile a una porzione di testo.
315|Il blocco style ospita regole CSS all’interno del documento HTML.
315|Un foglio esterno può essere condiviso da più pagine attraverso il collegamento link.
320|Una classe è riutilizzabile: più elementi possono avere lo stesso valore di class.
320|Un identificativo id deve essere unico all’interno del documento HTML.
316|Il selettore di tipo, per esempio p, seleziona gli elementi di quel tipo.
318|Il box model descrive contenuto, spaziatura interna, bordo e margine esterno.
318|Il padding è lo spazio tra il contenuto e il bordo dell’elemento.
318|Il margin è lo spazio esterno al bordo, distinto dal padding.
316|CSS accetta diversi formati di colore, inclusi nomi, valori esadecimali e RGB.
316|Le proprietà tipografiche regolano famiglia, dimensione, peso e altri aspetti del testo.
326|Un form raggruppa controlli con cui raccogliere dati; per elaborarli occorre una logica applicativa.
327|Un input text consente di inserire una stringa di testo su una riga.
328|L’input email può controllare la forma dell’indirizzo, ma non prova che la casella esista.
328|L’input date permette l’inserimento di una data; l’interfaccia concreta dipende dal browser.
329|required indica al browser che il controllo deve essere compilato prima dell’invio ordinario del form.
294|Nel normale HTML i nomi dei tag non distinguono maiuscole e minuscole; usare minuscole mantiene coerenza.
299|I titoli devono rappresentare la gerarchia del contenuto, oltre alla presentazione grafica.
320|Le classi CSS possono essere applicate a più elementi per condividere uno stile.
320|Duplicare un id nello stesso documento rende l’identificazione ambigua.
318|Lo spazio esterno è il margine; il padding è interno al bordo.
326|I controlli del form raccolgono valori, che possono poi essere inviati o elaborati.
329|La validazione required è un controllo del browser e non sostituisce verifiche sui dati ricevuti dal server.
315|Un foglio esterno centralizza le regole CSS e ne facilita il riuso.
316|La notazione esadecimale è uno dei modi disponibili per esprimere un colore CSS.''',
'b2': '''351|La lettera commerciale organizza mittente, destinatario, oggetto, messaggio e firma in modo riconoscibile.
364|La stampa unione combina un documento principale con un’origine dati per produrre documenti personalizzati.
364|L’origine dati contiene record e campi, mentre il documento principale contiene testo comune e campi unione.
370|L’anteprima consente di passare tra i record e controllare la personalizzazione prima della produzione finale.
394|Google Moduli organizza questionari e raccoglie le risposte in forma digitale.
395|Temi e impostazioni visuali cambiano l’aspetto del questionario senza cambiarne necessariamente le domande.
378|Campi e modelli aiutano a compilare documenti ricorrenti in modo coerente e con meno operazioni ripetitive.
364|Documento principale e origine dati sono i due componenti fondamentali della stampa unione.
351|Oggetto e firma aiutano a comprendere il tema della comunicazione e a identificare il mittente.
403|Le risposte inviate vengono raccolte e rese consultabili dal proprietario del modulo.
351|L’intestazione rende riconoscibile il mittente e le informazioni dell’organizzazione.
351|L’indirizzo del destinatario identifica a chi è rivolta la comunicazione.
351|La data colloca la comunicazione nel tempo e aiuta a ricostruire la corrispondenza.
351|I riferimenti permettono di collegare la lettera a pratiche o comunicazioni precedenti.
349|Il corpo deve comunicare lo scopo con chiarezza, precisione e tono adeguato al destinatario.
351|La formula di chiusura conclude la comunicazione in modo coerente con il registro della lettera.
351|La firma identifica chi assume la comunicazione e può indicarne il ruolo.
351|L’indicazione degli allegati permette al destinatario di verificarne la presenza.
380|La carta intestata raccoglie gli elementi identificativi ricorrenti dell’organizzazione.
378|Un modello riutilizzabile riduce il lavoro ripetitivo e mantiene struttura e formattazione coerenti.
383|I campi modulo delimitano zone di inserimento e guidano la compilazione del documento.
388|Un campo calcolato produce un risultato a partire da dati e da una formula prevista nel modello.
379|Gli strumenti di sviluppo permettono di inserire controlli nei documenti automatizzati.
383|Un elenco di valori predefiniti aiuta l’utente a scegliere tra alternative ammesse.
364|Per la stampa unione occorrono un modello comune e un elenco strutturato di destinatari.
365|I campi unione sono segnaposto: vengono sostituiti con i valori dei singoli record.
370|L’anteprima aiuta a rilevare campi mancanti e problemi di impaginazione prima di finalizzare.
366|La selezione dei destinatari limita la produzione ai record che rispettano i criteri scelti.
355|Le informazioni del destinatario devono essere disposte in modo chiaro per agevolare la consegna.
403|Le risposte sono raccolte dopo l’invio; la consultazione richiede l’accesso al modulo e alla rete.
400|Scelta multipla e caselle di controllo permettono rispettivamente una scelta esclusiva e più selezioni.
351|La data è un riferimento utile per identificare e contestualizzare una lettera commerciale.
351|Elencare gli allegati aiuta il destinatario a controllare la completezza della comunicazione.
383|Un controllo di inserimento può guidare l’utente verso il tipo di dato richiesto.
388|Un campo calcolato usa una formula; non è soltanto un’etichetta statica.
364|Nella produzione di lettere la stampa unione genera personalizzazioni in base ai record selezionati.
365|I segnaposto sono sostituiti con i dati durante la generazione dei documenti personalizzati.
366|Un filtro limita i destinatari senza dover cancellare definitivamente i record dall’origine dati.
394|Il servizio Google Moduli si usa online: non è presentato come applicazione esclusivamente offline.
403|Le risposte diventano consultabili dopo l’invio da parte degli utenti.''',
'b3': '''408|Il foglio di calcolo permette di organizzare dati e applicare formule per analisi e documenti aziendali.
421|I filtri selezionano le righe da visualizzare; i subtotali riepilogano gruppi di dati.
425|La formattazione condizionale applica uno stile quando è verificata una regola, senza cambiare il valore della cella.
411|SOMMA.SE somma valori in base a un criterio; CONTA.SE conta quelli che lo soddisfano.
438|Un modello protetto guida l’inserimento e limita modifiche involontarie alle celle di calcolo.
408|I due punti definiscono un intervallo: B2:B2202 comprende la colonna B dalla riga 2 alla riga 2202.
450|Le tabelle aiutano a pianificare costi, attività e risultati di iniziative commerciali e promozionali.
423|Il filtro cambia le righe visualizzate, non cancella quelle escluse dalla vista.
436|La protezione del foglio fa rispettare il blocco delle celle secondo le autorizzazioni impostate.
411|CONTA.SE applica un criterio; non equivale al conteggio indiscriminato di tutte le celle.
420|Ogni cella è individuata dall’incrocio tra una riga e una colonna.
420|A1 identifica la colonna A e la riga 1, non l’intera colonna o il foglio.
432|La barra della formula permette di leggere e modificare il contenuto della cella attiva.
432|Una cartella di lavoro può contenere più fogli, ciascuno con la propria griglia di celle.
408|SOMMA aggiunge i valori numerici dell’intervallo indicato.
414|La media aritmetica è la somma dei valori divisa per il loro numero.
414|Il massimo e il minimo sono valori estremi; non corrispondono alla media o alla somma.
411|Il conteggio numerico considera le celle contenenti numeri, distinguendole da testo e celle vuote.
408|SE valuta una condizione e sceglie tra due esiti in base al risultato logico.
411|E richiede che tutte le condizioni siano vere; O richiede che almeno una sia vera.
408|SOMMA.SE seleziona i valori che rispettano il criterio e ne calcola la somma.
408|Un riferimento relativo si sposta in relazione allo spostamento della formula copiata.
408|Il simbolo dollaro blocca la componente di riga o colonna che precede: $A$1 blocca entrambe.
421|L’ordinamento dispone i record secondo uno o più criteri mantenendo insieme i dati della stessa riga.
420|I duplicati devono essere valutati sul contenuto e sul significato dei record, prima dell’eventuale rimozione.
424|Il formato determina come il valore viene visualizzato; un formato data rappresenta una data secondo la notazione scelta.
424|Un valore pari a 0,25, visualizzato in percentuale, corrisponde al 25%.
424|Bordi e sfondi possono rendere riconoscibili intestazioni e gruppi di dati, migliorando la lettura.
432|Bloccare i riquadri mantiene visibili determinate righe o colonne durante lo scorrimento.
432|L’area di stampa e la ripetizione delle intestazioni aiutano a rendere leggibili le pagine stampate.
436|La protezione del foglio limita le modifiche delle celle; non equivale alla cifratura del file.
408|Il segno uguale introduce normalmente una formula nel foglio di calcolo.
408|SOMMA ignora le celle vuote nell’intervallo: non occorre riempirle tutte con zero.
408|Il riferimento assoluto $A$1 mantiene fissa riga e colonna durante la copia ordinaria della formula.
421|Ordinare significa cambiare la disposizione dei record rispetto al criterio scelto.
424|La formattazione cambia la visualizzazione, non il valore memorizzato.
408|SE restituisce l’esito associato a vero oppure a falso per la condizione impostata.
459|Un grafico collegato a un intervallo riflette le modifiche ai dati di quell’intervallo.
436|Il blocco delle celle ha effetto quando la protezione del foglio è attiva.
414|MEDIA restituisce una media, mentre SOMMA restituisce il totale.''',
'b4': '''470|Il microfono converte variazioni di pressione sonora in un segnale elettrico utilizzabile per la registrazione.
475|Campionamento e quantizzazione trasformano una grandezza continua in una rappresentazione discreta.
479|Selezioni e livelli consentono di isolare elementi e combinarli senza modificare ogni parte insieme.
510|Shotcut è presentato come software per montare ed elaborare video con strumenti di taglio, filtri e timeline.
502|Didascalie e riconoscimenti accompagnano il contenuto e possono indicare autori e contributi; non sostituiscono i permessi di utilizzo.
473|Formato e compressione influenzano dimensioni, compatibilità e qualità dei contenuti digitali.
466|La produzione multimediale deve considerare destinazione, pubblico e condizioni d’uso del materiale.
470|Un trasduttore converte una forma di segnale in un’altra: il microfono converte il suono in segnale elettrico.
473|La compressione riduce il volume dei dati; il compromesso con la qualità dipende dal metodo e dalle impostazioni.
502|I riconoscimenti documentano i contributi; la citazione degli autori non rende automaticamente autorizzato ogni riuso.
473|Il pixel è un elemento della griglia che rappresenta un’immagine raster.
474|La profondità di colore indica i bit dedicati alla rappresentazione del colore e influenza i valori disponibili.
468|La frequenza di campionamento indica quanti campioni vengono acquisiti in un secondo e si misura in hertz.
469|MP3 è un formato audio con compressione con perdita, utile a ridurre il volume dei dati.
469|WAV è un contenitore audio spesso usato con dati PCM non compressi; non impone sempre una sola codifica.
473|MP4 è un contenitore multimediale comune che può includere flussi audio e video.
486|GIF può contenere una sequenza animata di fotogrammi; non ogni file GIF è necessariamente animato.
486|PNG supporta la trasparenza ed è adatto anche a elementi grafici per il web.
486|Ridimensionare cambia larghezza e altezza in pixel; l’eventuale ricampionamento modifica la griglia dell’immagine.
481|Il ritaglio conserva una porzione dell’immagine ed elimina le parti esterne alla selezione.
485|La rotazione cambia l’orientamento e può correggere un orizzonte inclinato.
485|Luminosità e contrasto intervengono sulla resa dei toni dell’immagine.
479|I livelli permettono di organizzare elementi sovrapposti e modificarli separatamente.
479|Un elemento testuale può essere collocato su un livello per gestirlo separatamente dall’immagine.
503|La pianificazione delle scene definisce una sequenza coerente prima del montaggio.
516|Tagliare una clip permette di eliminare parti non necessarie e regolarne la durata.
516|Le transizioni regolano il passaggio tra clip; vanno scelte in relazione al ritmo e al messaggio.
502|Titoli iniziali e finali possono presentare il contenuto e indicare contributi e riconoscimenti.
522|L’esportazione produce un file multimediale fruibile, distinto dal progetto modificabile nell’editor.
475|16:9 esprime il rapporto tra larghezza e altezza; non è un numero di pixel.
521|Il bilanciamento audio mantiene comprensibile la voce rispetto a musica ed effetti.
486|La trasparenza permette di comporre un elemento PNG sopra sfondi diversi.
469|MP3 usa compressione audio con perdita di informazioni per ridurre i dati.
469|A parità di durata e caratteristiche, un WAV PCM non compresso occupa in genere più spazio di un MP3 compresso.
481|Il crop rimuove le porzioni esterne all’area scelta; non ingrandisce il contenuto per definizione.
479|I livelli sono elementi sovrapposti che permettono un controllo separato delle parti della composizione.
503|Pianificare le scene aiuta a mantenere coerenza tra messaggio, inquadrature e montaggio.
475|Un’immagine 16:9 ha larghezza superiore all’altezza: è un rapporto panoramico.
502|Titoli e didascalie possono fornire contesto e spiegazioni utili allo spettatore.
516|Una transizione collega due clip; non è necessariamente richiesta a ogni taglio.'''
}

# Editorial corrections: ambiguous, absolute, out-of-chapter and obsolete statements.
FIX = {
'a6-q01': ('L’AOO nella gestione documentale della PA è…', ['un insieme di uffici e servizi con regole omogenee di gestione documentale','un software antivirus','un singolo documento protocollato','un formato di fattura'],0),
'a6-q08': ('La fattura elettronica strutturata è distinta da una semplice scansione della fattura.',None,True),
'a6-q09': ('Un pagamento PagoPA può essere documentato da una ricevuta.',None,True),
'a6-q10': ('Un’identità SPID può essere usata per accedere a più servizi aderenti.',None,True),
'a6-q14': ('Il documento informatico rappresenta…',['atti, fatti o dati in forma digitale','soltanto fotografie prive di testo','esclusivamente copie stampate','solo i dati delle pagine social'],0),
'a6-q15': ('L’accettazione di un documento nella PA richiede…',['controlli e passaggi previsti dal flusso documentale','la cancellazione dei riferimenti','soltanto il cambio del nome del file','la conversione obbligatoria in immagine'],0),
'a6-q17': ('Il titolario serve a…',['classificare i documenti secondo le funzioni dell’ente','calcolare i pagamenti','generare password','firmare automaticamente ogni file'],0),
'a6-q19': ('I dati del 730 precompilato devono essere…',['verificati e, se necessario, integrati','accettati sempre senza controllo','eliminati prima di leggerli','sostituiti con dati casuali'],0),
'a6-q21': ('L’approvvigionamento elettronico riguarda…',['l’acquisto di beni e servizi attraverso strumenti digitali','soltanto la vendita tra privati','solo l’invio di newsletter','l’archiviazione delle password'],0),
'a6-q22': ('Gli strumenti di acquisto nel MePA servono a…',['gestire procedure di approvvigionamento','montare contenuti video','definire fogli di stile','creare reti private'],0),
'a6-q23': ('Le informazioni di recapito della fattura servono a…',['indirizzarla al destinatario attraverso lo SDI','calcolare la risoluzione delle immagini','assegnare un voto al fornitore','cambiare il codice ATECO'],0),
'a6-q24': ('Una scansione della fattura rispetto al file XML…',['non ne sostituisce la struttura dei dati','è sempre lo stesso formato','contiene automaticamente gli stessi campi strutturati','rende inutile lo SDI'],0),
'a6-q25': ('Il workflow documentale descrive…',['il percorso del documento tra attività e soggetti','il colore del documento','solo il suo peso in byte','soltanto il nome dell’autore'],0),
'a6-q26': ('L’abilitazione di un’impresa al MePA permette di…',['operare nelle categorie e secondo i requisiti previsti','accedere senza requisiti a ogni servizio pubblico','eliminare la contabilità','evitare ogni procedura di acquisto'],0),
'a6-q27': ('Il secondo livello SPID aggiunge alla password…',['un ulteriore fattore di verifica','un secondo nome utente pubblico','il codice di un prodotto','un numero di protocollo'],0),
'a6-q28': ('L’identificazione digitale permette al servizio di…',['riconoscere l’utente che chiede accesso','modificare i prezzi delle fatture','eliminare l’autenticazione','cambiare le funzioni del browser'],0),
'a6-q30': ('Il responsabile della gestione documentale si occupa di…',['coordinare regole e attività sui documenti','gestire esclusivamente la pubblicità','progettare soltanto i cavi di rete','elaborare solo file audio'],0),
'a6-q31': ('Nell’accesso con SPID, il gestore dell’identità…',['verifica le credenziali secondo il livello richiesto','crea automaticamente tutte le fatture','assegna un protocollo a ogni immagine','sostituisce il servizio pubblico richiesto'],0),
'a6-q33': ('La conservazione digitale coincide con il semplice salvataggio di un file in una cartella.',None,False),
'a6-q37': ('Tutti i livelli SPID prevedono esattamente gli stessi requisiti di autenticazione.',None,False),
'a6-q39': ('Il titolario aiuta a classificare i documenti secondo criteri condivisi.',None,True),
'b1-q02': ('Quale elemento HTML rappresenta un paragrafo?',['<p>','<table>','<img>','<form>'],0),
'b1-q09': ('La proprietà CSS text-align può controllare l’allineamento del testo.',None,True),
'b1-q33': ('I titoli HTML devono rappresentare una gerarchia coerente dei contenuti.',None,True),
'b1-q30': ('L’input di tipo date serve a…',['inserire una data','inserire un indirizzo email','selezionare un file video','assegnare una classe CSS'],0),
'b2-q03': ('Nella stampa unione, l’origine dati contiene…',['record e campi dei destinatari','soltanto il testo comune della lettera','solo le impostazioni della stampante','il correttore ortografico'],0),
'b2-q12': ('Il blocco destinatario di una lettera contiene…',['nome e indirizzo di chi riceve','soltanto la data di stampa','la password del mittente','solo il numero di allegati'],0),
'b2-q19': ('La carta intestata contiene…',['elementi identificativi ricorrenti dell’organizzazione','solo l’elenco delle fatture insolute','soltanto il nome del destinatario','esclusivamente il numero di pagina'],0),
'b2-q21': ('I campi modulo in Word permettono di…',['predisporre zone guidate di inserimento','trasformare ogni documento in un video','eliminare la necessità di compilare i dati','unire automaticamente due reti'],0),
'b2-q22': ('Un campo calcolato in un documento…',['restituisce un risultato sulla base di una formula','contiene sempre e soltanto testo fisso','elimina ogni dato inserito','sostituisce il nome del destinatario con un’immagine'],0),
'b2-q23': ('Gli strumenti di sviluppo di Word possono servire a…',['inserire controlli per documenti automatizzati','gestire solo i colori della stampante','assegnare indirizzi IP','pubblicare annunci'],0),
'b2-q24': ('Un elenco a discesa in un modulo serve a…',['scegliere tra valori predefiniti','scrivere sempre testo senza limiti','eliminare ogni controllo sui dati','convertire il testo in audio'],0),
'b2-q29': ('Un indirizzo ben disposto sulla busta aiuta a…',['identificare il destinatario e agevolare la consegna','calcolare la media delle vendite','generare il corpo della lettera','creare l’origine dati'],0),
'b2-q30': ('Google Moduli raccoglie le risposte…',['quando vengono inviate dagli utenti','prima che l’utente apra il modulo','solo dopo la stampa su carta','senza alcuna compilazione'],0),
'b2-q31': ('Per consentire più risposte nella stessa domanda di Google Moduli si usano…',['caselle di controllo','una scelta esclusiva','solo un campo data','un titolo di sezione'],0),
'b2-q34': ('I controlli dei moduli possono guidare l’inserimento dei dati.',None,True),
'b2-q35': ('Un campo calcolato può produrre un valore a partire da una formula.',None,True),
'b2-q36': ('Nella stampa unione di lettere, ogni record selezionato può generare una lettera personalizzata.',None,True),
'b2-q40': ('Le risposte di un modulo diventano consultabili dopo il loro invio.',None,True),
'b3-q21': ('SOMMA.SE permette di…',['sommare valori che rispettano un criterio','ordinare tutte le righe in ordine alfabetico','cambiare il colore di ogni cella','contare soltanto il numero dei fogli'],0),
'b3-q32': ('Il segno = viene usato per introdurre una formula in Excel.',None,True),
'b4-q05': ('Aggiungere didascalie e riconoscimenti a un video permette di…',['dare contesto e indicare i contributi','ottenere automaticamente ogni licenza','eliminare la necessità di montaggio','ridurre sempre la durata del video'],0),
'b4-q07': ('Prima di produrre un audiovisivo aziendale occorre considerare…',['pubblico, messaggio e contesto di fruizione','solo la durata più lunga possibile','soltanto il numero di file','solo la velocità del mouse'],0),
'b4-q10': ('Citare un autore nei titoli non sostituisce i permessi necessari per usare il materiale.',None,True),
'b4-q13': ('La frequenza di campionamento audio indica…',['il numero di campioni acquisiti al secondo','il volume massimo delle casse','il numero di canali televisivi','le dimensioni in pixel'],0),
'b4-q15': ('Un file WAV con audio PCM non compresso…',['conserva campioni audio senza compressione con perdita','è necessariamente più piccolo di un MP3 equivalente','contiene solo immagini','è un foglio di calcolo'],0),
'b4-q16': ('MP4 è…',['un contenitore multimediale che può includere audio e video','un editor di immagini','un protocollo di posta','un tipo di formula'],0),
'b4-q17': ('Il formato GIF può contenere…',['una sequenza animata di fotogrammi','soltanto registrazioni audio','formule contabili','dati di protocollo'],0),
'b4-q25': ('Pianificare la sequenza delle scene prima del montaggio aiuta a…',['dare coerenza al messaggio del video','aumentare obbligatoriamente la durata','eliminare la necessità di riprese','sostituire ogni file audio'],0),
'b4-q34': ('A parità di durata, un WAV PCM non compresso è sempre più piccolo di un MP3 equivalente.',None,False),
'b4-q37': ('Pianificare le scene aiuta a costruire una sequenza coerente.',None,True),
}
legacy=json.loads((ROOT/'content/legacy/original-bank.json').read_text(encoding='utf-8'))
metadata={
'a6':('PA digitale e servizi online','Documenti, fatture elettroniche, acquisti pubblici, SPID e pagamenti.',242,283),
'b1':('Siti web, HTML e CSS','Struttura delle pagine, stile, moduli e gestione dei contenuti.',284,347),
'b2':('Documenti aziendali e moduli','Lettere commerciali, stampa unione e documenti automatizzati.',348,407),
'b3':('Excel per l’azienda','Funzioni, analisi dei dati, modelli protetti e applicazioni commerciali.',408,465),
'b4':('Immagini, audio e video','Dalla rappresentazione digitale all’elaborazione e al montaggio.',466,525)}
for m in legacy['modules']:
    if m['id'] not in metadata:continue
    mid=m['id']; title,description,first,last=metadata[mid]
    notes=NOTES[mid].splitlines();assert len(notes)==40,(mid,len(notes))
    module=dict(id=mid,title=title,description=description,book_pages=[first,last],questions=[])
    for q,note in zip(m['questions'],notes):
        page,explanation=note.split('|');page=int(page)
        if q['id'] in FIX:
            q['q'],opts,q['answer']=FIX[q['id']]
            if opts is not None:q['options']=opts;q['type']='multiple'
            else:q['type']='truefalse'
        options=q['options'] if q['type']=='multiple' else ['Vero','Falso']
        answer=q['answer'] if q['type']=='multiple' else 0 if q['answer'] else 1
        module['questions'].append(dict(id=q['id'],q=q['q'],options=options,answer=answer,explanation=explanation,topic=title,difficulty='base',source=f'InfoComm, ed. 2021 · p. {page} (PDF p. {page+16})',bookPage=page,pdfPage=page+16,type=q['type']))
    modules.append(module)
bank=dict(version='2026.09.30-v2',edition='InfoComm, Hoepli, 2021',modules=modules)
out=ROOT/'public/data';out.mkdir(parents=True,exist_ok=True)
for m in modules:
    assert len(m['questions'])==40,(m['id'],len(m['questions']))
    for q in m['questions']:
        assert len(q['options']) in (2,4) and len(set(q['options']))==len(q['options']),q['id']
        assert 0<=q['answer']<len(q['options']) and first is not None
    (out/f"{m['id']}.json").write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
assert len(modules)==10
(out/'quiz.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Compiled {sum(len(m["questions"]) for m in modules)} questions in {len(modules)} modules.')
