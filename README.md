# InfoComm Quiz

Piattaforma didattica statica e gratuita per i Servizi commerciali / Web Community, basata sui percorsi di **InfoComm, Camagni e Nikolassy, Hoepli, edizione 2021**.

- [Apri la piattaforma](https://antoniorasulo89.github.io/infocomm-quiz/)
- [Strumenti docente](https://antoniorasulo89.github.io/infocomm-quiz/?view=teacher)
- [Guida e privacy](https://antoniorasulo89.github.io/infocomm-quiz/?view=guide)

## Funzioni

10 moduli, 400 domande con spiegazioni e riferimenti al libro. Allenamento con feedback immediato, simulazione con timer assoluto e consegna automatica, ripasso degli errori, salvataggio locale e recupero della prova. Cronologia delle ultime 100 prove, backup/importazione, export individuale JSON e stampa dei risultati.

Il docente può configurare numero di domande, durata, soglia e nome della prova; il link conserva un seme casuale per riprodurre domande e opzioni nello stesso ordine. Sono disponibili stampa della prova, correttore, importazione dei risultati degli studenti e riepilogo CSV. La configurazione viene mostrata prima dell’avvio. Il timer individuale parte quando lo studente avvia la prova.

Nessun account, backend, database, analytics, font remoto o servizio a pagamento. I dati didattici restano nel browser. Il nome eventualmente inserito viene scritto solo nel file scaricato. L’hosting può gestire i normali log HTTP.

## Avvio e aggiornamento

Richiede Node.js 22.12+ e Python 3.10+ per ricompilare la banca.

```sh
npm ci
python scripts/build_content.py
npm run dev
```

```sh
npm test
npm run build
npm run preview
```

La build produce `docs/`, pronta da pubblicare senza server applicativo. La configurazione esistente di GitHub Pages usa `master` e `/docs`: dopo un aggiornamento dei sorgenti, rigenerare e includere `docs/` nel commit. Non occorre un dominio a pagamento.

## Struttura

- `src/core.ts`: generazione deterministica delle prove, punteggio, timer, validazione dei risultati.
- `src/main.ts`: interfaccia e flussi studente/docente.
- `src/storage.ts`: persistenza locale con gestione degli errori.
- `src/style.css`: layout responsive, focus, stampa.
- `content/bank.txt`: domande rielaborate dei moduli A1–A5, con quesiti a scelta multipla e vero/falso.
- `content/legacy/original-bank.json`: banca precedente conservata come sorgente per A6 e B1–B4.
- `scripts/build_content.py`: compilazione e correzioni editoriali dei moduli mantenuti, spiegazioni e riferimenti.
- `public/data/`: banca completa e file per modulo, generati dallo script.
- `tests/`: test del motore e dei flussi browser.

Il PDF del libro non è incluso né necessario all’esecuzione. Nel PDF fornito la pagina stampata N corrisponde alla pagina PDF N+16. Le domande sono materiale didattico del progetto, non prove ufficiali INVALSI. I contenuti tecnologici seguono l’edizione 2021; non sono una guida aggiornata alle versioni dei prodotti o alla normativa.

## Verifica browser

Con la preview attiva sulla porta 4173:

```sh
npx playwright install chromium
node tests/browser.mjs
```

Si possono impostare `TEST_URL` e `CHROMIUM_PATH` per un altro indirizzo o un browser locale. Gli screenshot e i file di verifica vengono scritti in `../../work/browser` rispetto al repository.

## Limiti espliciti

Le soluzioni sono distribuite al browser e sono ispezionabili. Non esiste un’area docente protetta né una certificazione dell’identità o del voto. I file dei risultati possono essere modificati: la verifica di formato e coerenza non ne prova l’autenticità. La piattaforma è pensata per studio ed esercitazioni o prove supervisionate.

Il salvataggio è legato al dispositivo e al browser: cancellarne i dati elimina i progressi. Non c’è sincronizzazione automatica. I file importati dal docente restano in memoria fino alla chiusura della pagina. La pagina deve essere caricata con una connessione; non è implementata una cache offline installabile.

I piani di hosting gratuiti dipendono dalle condizioni del fornitore; l’app rimane trasferibile a qualsiasi hosting statico. Nessun servizio a consumo è richiesto.
