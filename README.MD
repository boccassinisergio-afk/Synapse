# Synapse

**🇮🇹 Italiano | [🇬🇧 English](#english)**

Un tool da riga di comando per tracciare concetti, argomenti e progressi di apprendimento. Costruito da zero, cresce insieme allo sviluppatore che lo ha creato.

<p align="center">
  <img src="synapse-demo.gif" alt="Synapse demo" width="700">
</p>

---

## Cos'è Synapse?

Synapse crea connessioni tra concetti. Ti permette di registrare cosa stai studiando, quanto bene lo comprendi e a che punto sei, tutto dal terminale, tutto salvato localmente in un file CSV.

L'idea: il tool cresce con te. Man mano che le tue competenze migliorano, migliora anche Synapse.

---

## Funzionalità

- Aggiungi voci di apprendimento con categoria, argomento, livello e stato
- ID generati automaticamente (nessun input manuale richiesto)
- Visualizza un report completo di tutti i concetti tracciati
- Cerca in tutti i campi con una parola chiave
- Aggiorna qualsiasi campo di una voce esistente
- Elimina voci tramite ID
- Gestione degli errori per ID mancanti in aggiornamento ed eliminazione
- I dati persistono tra le sessioni tramite un file CSV locale

---

## Campi

| Campo       | Descrizione                                   |
|-------------|-----------------------------------------------|
| `id`        | Identificatore univoco generato automaticamente |
| `categoria` | Area di studio (es. python, machine learning) |
| `argomento` | Argomento specifico (es. funzioni, regressione) |
| `livello`   | Livello di difficoltà (es. base, intermedio)  |
| `stato`     | Stato attuale (es. completato, in corso)      |
| `note`      | Note libere (es. nome del corso, settimana)   |

---

## Utilizzo

```bash
python Synapse_v2_1.py
```

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            SYNAPSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1) Aggiungi valore
2) Leggi report
3) Modifica valore
4) Cancella valore
5) Exit
```

Nella visualizzazione del report puoi mostrare tutte le voci oppure cercare per parola chiave, la ricerca esamina tutti i campi contemporaneamente.

---

## Esempio di voce

```
ID: 1 | Categoria: python | Argomento: funzioni | Livello: base | Stato: completato | Note: cs50p week2
```

---

## Architettura

Ogni record è modellato come un oggetto `SynapseEntry` invece che come un dizionario grezzo. La classe è l'unica definizione autorevole della struttura di una voce, e il resto del programma costruisce, legge e scrive quegli oggetti.

- `__init__` imposta i sei attributi per una nuova voce
- `@property` espone `id` come sola lettura, sostenuto da `_id` e sempre memorizzato come `int`
- `@classmethod from_dict()` è un costruttore alternativo che costruisce un'istanza a partire da una riga CSV
- `to_dict()` serializza un'istanza di nuovo in un dizionario per `csv.DictWriter`
- `__str__` definisce come viene stampata una voce, così `print(entry)` sostituisce la vecchia funzione di visualizzazione

Il flusso dei dati nel programma è: riga CSV -> dict -> `SynapseEntry` -> dict -> riga CSV. L'accesso dinamico ai campi all'interno dei cicli è gestito con `getattr` e `setattr`, mantenendo simmetrici i percorsi di lettura e scrittura.

---

## Stack tecnico

- Python 3.12+
- Moduli `csv`, `os`, `sys` (libreria standard)
- Design orientato agli oggetti, nessuna dipendenza esterna

---

## Contesto del progetto

Synapse è stato costruito durante [CS50P](https://cs50.harvard.edu/python/) - il corso introduttivo alla programmazione in Python di Harvard - come parte di un percorso autodidatta partito da zero verso lo sviluppo AI.

Il progetto vive anche in [`cs50p-python`](https://github.com/boccassinisergio-afk/cs50p-python), un repo pubblico che documenta l'intero percorso di apprendimento.

---

## Changelog

### v2.1
- Refactoring da un design procedurale a uno orientato agli oggetti
- Introdotta la classe `SynapseEntry` per modellare ogni record come oggetto
- Aggiunti `@property` per un `id` di sola lettura, `@classmethod from_dict()` come costruttore alternativo, `to_dict()` per la serializzazione e `__str__` per la visualizzazione
- Sostituita la funzione standalone `print_row()` con il metodo `__str__`
- Le funzioni ora operano su istanze `SynapseEntry`, con `getattr`/`setattr` per l'accesso dinamico ai campi

### v1.1
- ID generati automaticamente tramite `auto_id()`, usa `max(existing_ids) + 1`, gestisce correttamente le eliminazioni
- Ricerca per parola chiave in tutti i campi nella visualizzazione del report
- Gestione degli errori in `update_value()` e `delete_value()` per ID mancanti
- Estratta `print_row()` come funzione riutilizzabile
- Miglioramenti generali di stabilità del codice

### v1.0
- Rilascio iniziale: aggiungi, visualizza, aggiorna, elimina voci

---

## Roadmap

- [ ] Filtra il report per categoria o stato
- [ ] Statistiche sui progressi
- [ ] Esportazione in Markdown o HTML
- [ ] Backend JSON
- [ ] ID basati su UUID

---

## Autore

Costruito da Sergio, in transizione verso lo sviluppo AI, un progetto alla volta.

<br><br>

---
---

<a name="english"></a>

# Synapse

**[🇮🇹 Italiano](#synapse) | 🇬🇧 English**

A command-line tool to track concepts, topics, and learning progress. Built from zero, growing alongside the developer who made it.

<p align="center">
  <img src="synapse-demo.gif" alt="Synapse demo" width="700">
</p>

---

## What is Synapse?

Synapse creates connections between concepts. It lets you log what you're studying, how well you understand it, and where you stand, all from the terminal, all saved locally in a CSV file.

The idea: the tool grows with you. As your skills improve, so does Synapse.

---

## Features

- Add learning entries with category, topic, level, and status
- Auto-generated IDs (no manual input required)
- View a full report of all tracked concepts
- Search across all fields with a keyword
- Update any field of an existing entry
- Delete entries by ID
- Error handling for missing IDs on update and delete
- Data persists across sessions via a local CSV file

---

## Fields

| Field       | Description                                   |
|-------------|-----------------------------------------------|
| `id`        | Auto-generated unique identifier              |
| `categoria` | Area of study (e.g. python, machine learning) |
| `argomento` | Specific topic (e.g. functions, regression)   |
| `livello`   | Difficulty level (e.g. base, intermedio)      |
| `stato`     | Current status (e.g. completato, in corso)    |
| `note`      | Free notes (e.g. course name, week)           |

---

## Usage

```bash
python Synapse_v2_1.py
```

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            SYNAPSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1) Aggiungi valore
2) Leggi report
3) Modifica valore
4) Cancella valore
5) Exit
```

When viewing the report, you can either show all entries or search by keyword, the search scans all fields simultaneously.

---

## Example Entry

```
ID: 1 | Categoria: python | Argomento: funzioni | Livello: base | Stato: completato | Note: cs50p week2
```

---

## Architecture

Each record is modeled as a `SynapseEntry` object rather than a raw dictionary. The class is the single authoritative definition of an entry's structure, and the rest of the program builds, reads, and writes those objects.

- `__init__` sets the six attributes for a new entry
- `@property` exposes `id` as read-only, backed by `_id` and always stored as an `int`
- `@classmethod from_dict()` is an alternative constructor that builds an instance from a CSV row
- `to_dict()` serializes an instance back into a dictionary for `csv.DictWriter`
- `__str__` defines how an entry is printed, so `print(entry)` replaces the old display function

The data flow across the program is: CSV row -> dict -> `SynapseEntry` -> dict -> CSV row. Dynamic field access inside loops is handled with `getattr` and `setattr`, keeping the read and write paths symmetrical.

---

## Tech Stack

- Python 3.12+
- `csv`, `os`, `sys` modules (standard library)
- Object-oriented design, no external dependencies

---

## Project Context

Synapse was built during [CS50P](https://cs50.harvard.edu/python/) - Harvard's Introduction to Programming with Python - as part of a self-directed path from zero background toward AI development.

The project lives even in [`cs50p-python`](https://github.com/boccassinisergio-afk/cs50p-python), a public repo documenting the full learning journey.

---

## Changelog

### v2.1
- Refactored from a procedural design to an object-oriented one
- Introduced the `SynapseEntry` class to model each record as an object
- Added `@property` for a read-only `id`, `@classmethod from_dict()` as an alternative constructor, `to_dict()` for serialization, and `__str__` for display
- Replaced the standalone `print_row()` function with the `__str__` method
- Functions now operate on `SynapseEntry` instances, with `getattr`/`setattr` for dynamic field access

### v1.1
- Auto-generated IDs via `auto_id()`, uses `max(existing_ids) + 1`, handles deletions correctly
- Keyword search across all fields in report view
- Error handling in `update_value()` and `delete_value()` for missing IDs
- Extracted `print_row()` as a reusable function
- General code stability improvements

### v1.0
- Initial release: add, view, update, delete entries

---

## Roadmap

- [ ] Filter report by category or status
- [ ] Progress statistics
- [ ] Export to Markdown or HTML
- [ ] JSON backend
- [ ] UUID-based IDs

---

## Author

Built by Sergio, transitioning into AI development, one project at a time.