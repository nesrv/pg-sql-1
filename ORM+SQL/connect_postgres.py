import psycopg2
from psycopg2 import Error

# Параметры подключения берутся из переменных окружения для безопасности
import os

try:
    # Установка соединения с базой данных
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "bookstore"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("postgres"),
        port=os.getenv("DB_PORT", "5433")
    )

    # Создание курсора для выполнения операций с базой данных
    cursor = connection.cursor()
    
    # Проверка соединения - вывод версии PostgreSQL
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"Подключено к PostgreSQL. Версия: {version[0]}")

except (Exception, Error) as error:
    print(f"Ошибка при подключении к PostgreSQL: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
