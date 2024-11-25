# Удаление данных. Команда DELETE

```sql
DELETE FROM имя_таблицы
[WHERE условие_удаления]

```

Например, удалим строки, у которых производитель - `Apple`:

```sql
DELETE FROM Products
WHERE Company='Apple';
```

Или удалим все товары, производителем которых является `HTC` и которые имеют цену меньше `35000`:

```sql
DELETE FROM Products
WHERE Company='HTC' AND Price < 15000;
```

Если необходимо вовсе удалить все строки вне зависимости от условия, то условие можно не указывать:

```sql
DELETE FROM Products;
```