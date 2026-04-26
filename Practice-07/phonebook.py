# phonebook.py
import csv
import psycopg2
from connect import get_connection

def create_table():
    """Создает таблицу при запуске, если её нет."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def sync_to_csv():
    """Сохраняет актуальное состояние базы в файл contacts.csv."""
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT username, phone FROM phonebook ORDER BY id;")
        rows = cur.fetchall()
        with open('contacts.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    except Exception as e:
        print(f"Ошибка синхронизации с CSV: {e}")
    finally:
        cur.close()
        conn.close()

def insert_contact(username, phone):
    """Добавляет или обновляет контакт и синхронизирует CSV."""
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO phonebook (username, phone) 
            VALUES (%s, %s) 
            ON CONFLICT (username) 
            DO UPDATE SET phone = EXCLUDED.phone;
        """, (username.strip(), phone.strip()))
        conn.commit()
        print(f"Контакт '{username}' сохранен.")
        sync_to_csv() # Обновляем файл
    except Exception as e:
        print(f"Ошибка: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def import_from_csv(filename):
    """Загружает данные из CSV в базу данных."""
    conn = get_connection()
    cur = conn.cursor()
    try:
        with open(filename.strip(), newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            count = 0
            for row in reader:
                if len(row) < 2: continue
                name, phone = row[0].strip(), row[1].strip()
                if not name or name.lower() == "username": continue
                
                cur.execute("""
                    INSERT INTO phonebook (username, phone) 
                    VALUES (%s, %s) 
                    ON CONFLICT (username) 
                    DO UPDATE SET phone = EXCLUDED.phone;
                """, (name, phone))
                count += 1
        conn.commit()
        print(f"Импорт завершен. Обработано строк: {count}")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    finally:
        cur.close()
        conn.close()

def delete_contact(val, by_phone=False):
    """Удаляет контакт и синхронизирует CSV."""
    conn = get_connection()
    cur = conn.cursor()
    sql = "DELETE FROM phonebook WHERE phone=%s" if by_phone else "DELETE FROM phonebook WHERE username=%s"
    cur.execute(sql, (val,))
    conn.commit()
    print("Контакт удален.")
    sync_to_csv() # Обновляем файл
    cur.close()
    conn.close()

def show_all_contacts():
    """Выводит список из базы."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username, phone FROM phonebook ORDER BY id;")
    rows = cur.fetchall()
    if not rows:
        print("\n[!] База пуста.")
    else:
        print("\n--- ТЕКУЩИЕ КОНТАКТЫ ---")
        for row in rows:
            print(f"ID: {row[0]} | Имя: {row[1]} | Тел: {row[2]}")
    cur.close()
    conn.close()

def menu():
    create_table()
    while True:
        print("\n1. Добавить/Обновить | 2. Импорт из CSV | 6. Удалить | 7. Показать все | 0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            insert_contact(input("Имя: "), input("Телефон: "))
        elif choice == "2":
            import_from_csv(input("Имя CSV файла (contacts.csv): "))
        elif choice == "6":
            val = input("Введите имя или телефон для удаления: ")
            mode = input("1 - по имени, 2 - по телефону: ")
            delete_contact(val, by_phone=(mode == "2"))
        elif choice == "7":
            show_all_contacts()
        elif choice == "0":
            break

if __name__ == "__main__":
    menu()