# InfoComm Quiz · stile INVALSI

Piattaforma gratuita di quiz dal libro **InfoComm Hoepli** (Servizi commerciali / Web Community), pubblicata con GitHub Pages.

- 🎓 Quiz: https://antoniorasulo89.github.io/infocomm-quiz/
- 👩‍🏫 Area docente (riservata): https://antoniorasulo89.github.io/infocomm-quiz/docente.html
- 📖 Guida docente: https://antoniorasulo89.github.io/infocomm-quiz/guida-docente.html

10 moduli per capitoli · banca dati di **40 domande per modulo (400 totali)** · timer configurabile con consegna automatica · soglia 6/10 · soluzioni con pagina del libro · nessun account, nessun dato online.

## Rigenerare la banca dati

Il file `docs/data/quiz.json` è generato dal PDF del libro (tenuto fuori dal repo):

```bat
mkdir dist
rem copia in dist\ il PDF "20315 - InfoComm.pdf"
python scripts\build_quiz_data.py
python scripts\smoke_quiz.py
```
