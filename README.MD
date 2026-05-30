# Synapse

A command-line tool to track concepts, topics, and learning progress. Built from zero, growing alongside the developer who made it.

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
python synapse.py
```

```
--- SYNAPSE MENU ---
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

## Tech Stack

- Python 3.12+
- `csv` module (standard library)
- No external dependencies

---

## Project Context

Synapse was built during [CS50P](https://cs50.harvard.edu/python/) - Harvard's Introduction to Programming with Python - as part of a self-directed path from zero background toward AI development.

The project lives in [`cs50p-python`](https://github.com/boccassinisergio-afk/cs50p-python), a public repo documenting the full learning journey.

---

## Changelog

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