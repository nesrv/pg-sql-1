from postgres_in_docker_connect import get_connection

## тест
connection = get_connection()
cursor = connection.cursor()

cursor.execute("SELECT version();")
version = cursor.fetchone()
print(f"Успешное подключение к PostgreSQL!")
print(f"Версия базы данных: {version[0]}")

sql_1 = '''
CREATE TABLE Products
(
    Id SERIAL PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Company VARCHAR(20) NOT NULL,
    ProductCount INTEGER DEFAULT 0,
    Price NUMERIC
);
 
INSERT INTO Products (ProductName, Company, ProductCount, Price)
VALUES
('iPhone X', 'Apple', 3, 36000),
('iPhone 8', 'Apple', 2, 41000),
('Galaxy S9', 'Samsung', 2, 46000),
('Galaxy S8 Plus', 'Samsung', 1, 56000),
('Desire 12', 'HTC', 5, 28000);
'''

cursor.execute(sql_1)
# поддверждаем транзакцию
connection.commit()
print("Таблица Products успешно создана")