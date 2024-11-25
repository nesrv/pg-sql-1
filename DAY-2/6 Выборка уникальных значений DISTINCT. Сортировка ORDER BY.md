# DISTINCT. Выборка уникальных значений


Оператор DISTINCT позволяет выбрать уникальные данные по определенным столбцам.

Например, в таблице товаров разные товары могут иметь одних и тех же производителей. Например, у нас следующая таблица:

[Файл 6-1.sql](sql/6-1.sql)

```sql
CREATE TABLE Products
(
    Id SERIAL PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Company VARCHAR(20) NOT NULL,
    ProductCount INTEGER DEFAULT 0,
    Price NUMERIC
);
INSERT INTO Products  (ProductName, Company, ProductCount, Price)
VALUES
('iPhone X', 'Apple', 2, 71000),
('iPhone 8', 'Apple', 3, 56000),
('Galaxy S9', 'Samsung', 6, 56000),
('Galaxy S8 Plus', 'Samsung', 2, 46000),
('Desire 12', 'HTC', 3, 26000);

```


Выберем всех производителей:

```sql
SELECT DISTINCT Company FROM Products;
```

# ORDER BY. Сортировка

```sql
SELECT * FROM Products
ORDER BY ProductCount;
```

Также можно производить упорядочивание данных по псевдониму столбца, который определяется с помощью оператора `AS`:

```sql
SELECT ProductName, ProductCount * Price AS TotalSum
FROM Products
ORDER BY TotalSum;
```

В качестве критерия сортировки также можно использовать сложно выражение на основе столбцов:

```sql
SELECT ProductName, Price, ProductCount
FROM Products
ORDER BY ProductCount * Price;
```

## Сортировка по убыванию

По умолчанию данные сортируются по возрастанию, однако с помощью оператора `DESC` можно задать сортировку по убыванию.


```sql
SELECT ProductName, Company
FROM Products
ORDER BY Company DESC;
```

По умолчанию вместо `DESC` используется оператор `ASC`, который сортирует по возрастанию:

```sql
SELECT ProductName, Company
FROM Products
ORDER BY Company ASC;
```

## Сотировка по нескольким столбцам


Если необходимо отсортировать сразу по нескольким столбцам, то все они перечисляются через запятую после оператора `ORDER BY`:


```sql
SELECT ProductName, Price, Company
FROM Products
ORDER BY Company, ProductName;
```



В этом случае сначала строки сортируются по столбцу `Company` по возрастанию. 

Затем если есть две строки, в которых столбец `Company` имеет одинаковое значение, то они сортируются по столбцу `ProductName` также по возрастанию. 

Но опять же с помощью `ASC` и `DESC` можно отдельно для разных столбцов определить сортировку по возрастанию и убыванию:


```sql
SELECT ProductName, Price, Company
FROM Products
ORDER BY Company ASC, ProductName DESC;
```