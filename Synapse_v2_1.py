import csv
import os
import sys


FILE_NAME = "value_r.csv"
FIELDNAMES = ["id", "categoria", "argomento", "livello", "stato", "note"]


def main():
    initialize()

    while True:
        print("\n--- SYNAPSE MENU ---")
        choice = input("1) Aggiungi valore\n2) Leggi report\n3) Modifica valore\n4) Cancella valore\n5) Exit\nScelta: ").strip()

        if choice == "1":
            add_value()
        elif choice == "2":
            view_report()
        elif choice == "3":
            update_value()
        elif choice ==  "4":
            delete_value()
        elif choice == "5":
            sys.exit()
        else:
            print("Scelta non valida.")


# ---------------- INITIALIZE ----------------
def initialize():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


# ---------------- ADD ----------------
def add_value():
    value_one = auto_id()
    value_two = input("Categoria: ").lower().strip()
    value_three = input("Argomento: ").lower().strip()
    value_four = input("Livello: ").lower().strip()
    value_five = input("Stato: ").lower().strip()
    value_six = input("Note: ").lower().strip()

    row = {
        FIELDNAMES[0]: value_one,
        FIELDNAMES[1]: value_two,
        FIELDNAMES[2]: value_three,
        FIELDNAMES[3]: value_four,
        FIELDNAMES[4]: value_five,
        FIELDNAMES[5]: value_six
    }

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(row)

    print("Synapse -- Valore aggiunto con successo.")


# ---------------- VIEW ----------------
def view_report():
    with open(FILE_NAME) as file:
        reader = csv.DictReader(file)

        print("\n--- Synapse -- REPORT ---")
        choice = input("Vuoi cercare una parola specifica? ( si, no): ").strip().lower()
        if choice == "no":
            for row in reader:
                print_row(row)
        elif choice == "si":
            keyword = input("Inserisci la parola da cercare: ").strip().lower()
            for row in reader:
                if any(keyword in row[field].lower() for field in FIELDNAMES[1:]):
                    print_row(row)

#---------------- MODIFY ---------------
def update_value():
    target = input("Quale ID vuoi modificare? ").strip()

    updated_rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["id"] == target:
                found = True 
                target_int = input("Quale attributo vuoi modificare? ").lower().strip()
                if target_int in FIELDNAMES[1:]:
                    new_value = input("Nuovo valore: ").strip()
                    row[target_int] = new_value

            updated_rows.append(row)

        if not found:
            print("Synapse -- ID non trovato.")
            return 

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(updated_rows)

    print("Synapse -- Aggiornamento completato.")
    
#--------------- DELETE --------------
def delete_value():
    target = input("Quale ID vuoi eliminare? ").strip()

    remaining_rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["id"] == target:
                found = True
            else:
                remaining_rows.append(row)

        if not found:
            print("Synapse -- ID non trovato.")
            return 

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(remaining_rows)

    print("Synapse -- Valore eliminato.")

#---------------- AUTO ID --------------------
def auto_id():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        ids = []

        for row in reader:
            try:
                ids.append(int(row["id"]))
            except ValueError:
                pass

        if not ids:
            return 1

        return max(ids) + 1
    
def print_row(row):
    print(
        f"ID: {row['id']} | "
        f"Categoria: {row['categoria']} | "
        f"Argomento: {row['argomento']} | "
        f"Livello: {row['livello']} | "
        f"Stato: {row['stato']} | "
        f"Note: {row['note']}"
    )
    
if __name__ == "__main__":
    main()