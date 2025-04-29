import psycopg2
from psycopg2 import Error

def get_connection():
    try:
        # Параметры подключения к базе в докере
        connection = psycopg2.connect(
            host="localhost",
            database="bookstore",
            user="postgres",
            password="postgres",
            port="5434"  # Порт из docker-compose.yml
        )
        return connection
    except (Exception, Error) as error:
        print(f"Ошибка при подключении к PostgreSQL: {error}")
        return None

