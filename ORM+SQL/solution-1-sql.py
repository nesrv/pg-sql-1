from psycopg2_connect import get_connection

## тест
connection = get_connection()
cursor = connection.cursor()

cursor.execute("SELECT version();")
version = cursor.fetchone()
print(f"Успешное подключение к PostgreSQL!")
print(f"Версия базы данных: {version[0]}")

sql_1 = '''
SELECT * from Products where price < 40000;
'''

cursor.execute(sql_1)
print(*cursor.fetchall(), sep='\n')