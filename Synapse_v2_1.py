import csv
import os
import sys


FILE_NAME = "value_r.csv"
FIELDNAMES = ["id", "categoria", "argomento", "livello", "stato", "note"]


class SynapseEntry:
    def __init__(self, id, categoria, argomento, livello, stato, note=""):
        self._id = int(id)
        self.categoria = categoria
        self.argomento = argomento
        self.livello = livello
        self.stato = stato
        self.note = note

    @property
    def id(self):
        return self._id

    @classmethod
    def from_dict(cls, row):
        return cls(
            id=row["id"],
            categoria=row["categoria"],
            argomento=row["argomento"],
            livello=row["livello"],
            stato=row["stato"],
            note=row["note"],
        )

    def to_dict(self):
        return {
            "id": self.id,
            "categoria": self.categoria,
            "argomento": self.argomento,
            "livello": self.livello,
            "stato": self.stato,
            "note": self.note,
        }

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Categoria: {self.categoria} | "
            f"Argomento: {self.argomento} | "
            f"Livello: {self.livello} | "
            f"Stato: {self.stato} | "
            f"Note: {self.note}"
        )


def main():
    initialize()

    while True:
        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("            SYNAPSE        ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        choice = input("1) Aggiungi valore\n2) Leggi report\n3) Modifica valore\n4) Cancella valore\n5) Exit\nScelta: ").strip()

        if choice == "1":
            add_value()
        elif choice == "2":
            view_report()
        elif choice == "3":
            update_value()
        elif choice == "4":
            delete_value()
        elif choice == "5":
            sys.exit()
        else:
            print("Scelta non valida.")


def initialize():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def add_value():
    entry = SynapseEntry(
        id=auto_id(),
        categoria=input("Categoria: ").lower().strip(),
        argomento=input("Argomento: ").lower().strip(),
        livello=input("Livello: ").lower().strip(),
        stato=input("Stato: ").lower().strip(),
        note=input("Note: ").lower().strip(),
    )

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(entry.to_dict())

    print("\n✓ Synapse -- Valore aggiunto con successo.")


def view_report():
    with open(FILE_NAME) as file:
        reader = csv.DictReader(file)

        print("\n--- Synapse -- REPORT ---")
        choice = input("Vuoi cercare una parola specifica? (si, no): ").strip().lower()

        if choice == "no":
            for row in reader:
                print(SynapseEntry.from_dict(row))
        elif choice == "si":
            keyword = input("Inserisci la parola da cercare: ").strip().lower()
            for row in reader:
                entry = SynapseEntry.from_dict(row)
                if any(keyword in getattr(entry, field).lower() for field in FIELDNAMES[1:]):
                    print(entry)


def update_value():
    target = input("Quale ID vuoi modificare? ").strip()
    updated_rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            entry = SynapseEntry.from_dict(row)
            if str(entry.id) == target:
                found = True
                field = input("Quale attributo vuoi modificare? ").lower().strip()
                if field in FIELDNAMES[1:]:
                    new_value = input("Nuovo valore: ").strip()
                    setattr(entry, field, new_value)
            updated_rows.append(entry.to_dict())

    if not found:
        print("\n✗ Synapse -- ID non trovato.")
        return

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(updated_rows)

    print("\n✓ Synapse -- Aggiornamento completato.")


def delete_value():
    target = input("Quale ID vuoi eliminare? ").strip()
    remaining_rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            entry = SynapseEntry.from_dict(row)
            if str(entry.id) == target:
                found = True
            else:
                remaining_rows.append(entry.to_dict())

    if not found:
        print("\n✗ Synapse -- ID non trovato.")
        return

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(remaining_rows)

    print("\n✓ Synapse -- Valore eliminato.")


def auto_id():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        ids = [int(row["id"]) for row in reader if row["id"].isdigit()]
    return max(ids) + 1 if ids else 1


if __name__ == "__main__":
    main()