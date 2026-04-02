# connect.py
import psycopg2
from config import host, database, user, password

def get_connection():
    """Создает и возвращает соединение с базой данных PostgreSQL."""
    return psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )