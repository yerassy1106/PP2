import psycopg2
from connect import get_connection

def call_upsert(name, phone):
    """Добавить или обновить один контакт"""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        conn.commit()
        print(f"[OK] Контакт {name} обработан.")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[Error] Upsert failed: {e}")

def call_bulk_insert(names_list, phones_list):
    """Массовая вставка списком"""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("CALL bulk_insert_contacts(%s, %s)", (names_list, phones_list))
        conn.commit()
        print(f"[OK] Массовая вставка завершена.")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[Error] Bulk insert failed: {e}")

def search_contacts(pattern):
    """Поиск по паттерну"""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
        results = cur.fetchall()
        print(f"\nРезультаты поиска ('{pattern}'):")
        for row in results:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[Error] Search failed: {e}")

def get_paginated(limit, offset):
    """Пагинация"""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
        results = cur.fetchall()
        print(f"\nСтраница (limit {limit}, offset {offset}):")
        for row in results:
            print(row)
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[Error] Pagination failed: {e}")

def call_delete(target):
    """Удаление"""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("CALL delete_contact(%s)", (target,))
        conn.commit()
        print(f"[OK] Контакт '{target}' удален (если он существовал).")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[Error] Delete failed: {e}")

if __name__ == "__main__":
    # --- ТЕСТЫ ---
    # 1. Одиночный Upsert
    call_upsert("Yersultan", "87015554433")

    # 2. Массовая вставка (один номер правильный, другой короткий - для теста)
    call_bulk_insert(["Miras", "Temir"], ["87021112233", "123"]) 

    # 3. Поиск
    search_contacts("Yer")

    # 4. Пагинация
    get_paginated(2, 0)

    # 5. Удаление
    # call_delete("Miras")