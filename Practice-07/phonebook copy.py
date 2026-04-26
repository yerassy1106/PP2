from connect import get_connection
import csv
from connect import get_connection

def insert_contact(username, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s) ON CONFLICT (username) DO NOTHING",
        (username, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

def search_by_name(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE username ILIKE %s", (f"%{name}%",))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def search_by_phone_prefix(prefix):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (prefix + "%",))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def update_contact(username, new_name=None, new_phone=None):
    conn = get_connection()
    cur = conn.cursor()

    if new_name:
        cur.execute(
            "UPDATE phonebook SET username=%s WHERE username=%s",
            (new_name, username)
        )

    if new_phone:
        cur.execute(
            "UPDATE phonebook SET phone=%s WHERE username=%s",
            (new_phone, username)
        )

    conn.commit()
    cur.close()
    conn.close()

def delete_contact_by_name(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE username=%s", (username,))

    conn.commit()
    cur.close()
    conn.close()

def delete_contact_by_phone(phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))

    conn.commit()
    cur.close()
    conn.close()

def import_from_csv(filename='contacts.csv'):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            username, phone = row
            cur.execute(
                "INSERT INTO phonebook (username, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                (username, phone)
            )

    conn.commit()
    cur.close()
    conn.close()

def import_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 2:
                continue  # пропускаем строки, где не два столбца
            name, phone = row
            cur.execute(
                "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                (name, phone)
            )

    conn.commit()
    cur.close()
    conn.close()
    print("CSV импортирован успешно!")

def menu():
    while True:
        print("\n1. Add contact")
        print("2. Import CSV")
        print("3. Search by name")
        print("4. Search by phone prefix")
        print("5. Update contact")
        print("6. Delete contact")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)

        elif choice == "2":
            file = input("CSV filename: ")
            import_from_csv(file)

        elif choice == "3":
            name = input("Search name: ")
            search_by_name(name)

        elif choice == "4":
            prefix = input("Phone prefix: ")
            search_by_phone_prefix(prefix)

        elif choice == "5":
            name = input("Current name: ")
            new_name = input("New name (or Enter): ")
            new_phone = input("New phone (or Enter): ")
            update_contact(name, new_name or None, new_phone or None)

        elif choice == "6":
            name = input("Delete by name: ")
            delete_contact_by_name(name)

        elif choice == "7":
            break 

if __name__ == "__main__":
    menu()