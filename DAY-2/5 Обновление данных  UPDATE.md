# Обновление данных. Команда UPDATE


Для обновления данных в базе данных `PostgreSQL` применяется команда `UPDATE`. 

Она имеет следующий общий формальный синтаксис:

```sql
UPDATE имя_таблицы
SET столбец1 = значение1, столбец2 = значение2, ... столбецN = значениеN
[WHERE условие_обновления]

```

Например, увеличим у всех товаров цену на `3000`:

```sql
UPDATE Products
SET Price = Price + 3000;
```


В данном случае обновление касается всех строк. 

С помощью выражения `WHERE` можно с помощью условию конкретизировать обновляемые строки - если строка соответствует условию, то она будет обновляться. 

Например, изменим название производителя с `"Samsung"` на `"Samsung Inc."`:

```sql
UPDATE Products
SET Manufacturer = 'Samsung Inc.'
WHERE Manufacturer = 'Samsung';
```

Также можно обновлять сразу несколько столбцов:


```sql
UPDATE Products
SET Manufacturer = 'Samsung',
    ProductCount = ProductCount + 3
WHERE Manufacturer = 'Samsung Inc.';
```