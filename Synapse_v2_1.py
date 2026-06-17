import csv
import os
import sys


FILE_NAME = "value_r.csv"
FIELDNAMES = ["id", "categoria", "argomento", "livello", "stato", "note"]


class SynapseEntry:

    """Represents a single knowledge entry in the Synapse tracker.

    Attributes:
        categoria (str): The knowledge category (e.g. 'python', 'linux').
        argomento (str): The specific topic within the category.
        livello (str): The proficiency level (e.g. 'base', 'intermedio').
        stato (str): The learning status (e.g. 'in corso', 'completato').
        note (str): Optional notes about the entry.
    """

    def __init__(self, id: int | str, categoria: str, argomento: str, livello: str, stato: str, note: str = "") -> None:
        self._id = int(id)
        self.categoria = categoria
        self.argomento = argomento
        self.livello = livello
        self.stato = stato
        self.note = note

    @property
    def id(self) -> int:
        return self._id

    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "SynapseEntry":
        
        """Create a SynapseEntry instance from a CSV row dictionary.

        Args:
            row (dict): A dictionary with keys matching FIELDNAMES.

        Returns:
            SynapseEntry: A new instance populated with row data.
        """

        return cls(
            id=row["id"],
            categoria=row["categoria"],
            argomento=row["argomento"],
            livello=row["livello"],
            stato=row["stato"],
            note=row["note"],
        )

    def to_dict(self) -> dict[str, str | int]:

        """Serialize the entry to a dictionary compatible with csv.DictWriter.

        Returns:
            dict: A dictionary mapping all field names to their current values.
        """

        return {
            "id": self.id,
            "categoria": self.categoria,
            "argomento": self.argomento,
            "livello": self.livello,
            "stato": self.stato,
            "note": self.note,
        }

    def __str__(self) -> str:

        """Return a formatted single-line string representation of the entry."""

        return (
            f"ID: {self.id} | "
            f"Categoria: {self.categoria} | "
            f"Argomento: {self.argomento} | "
            f"Livello: {self.livello} | "
            f"Stato: {self.stato} | "
            f"Note: {self.note}"
        )


def main() -> None:

    """Run the Synapse CLI loop: initialize storage and dispatch user actions."""

    initialize()

    """Create the CSV file with headers if it does not already exist."""

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


def initialize() -> None:
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def add_value() -> None:

    """Prompt the user for all entry fields and append a new entry to the CSV file."""

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


def view_report() -> None:

    """Display all entries, with optional keyword filtering across all non-ID fields."""

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


def update_value() -> None:

    """Find an entry by ID and overwrite one of its fields with a new value."""

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


def delete_value() -> None:

    """Remove an entry from the CSV file by its ID, rewriting the file without it."""

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


def auto_id() -> int:

    """Generate the next available integer ID based on existing entries.

    Returns:
        int: The highest existing ID plus one, or 1 if the file is empty.
    """

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        ids = [int(row["id"]) for row in reader if row["id"].isdigit()]
    return max(ids) + 1 if ids else 1


if __name__ == "__main__":
    main()