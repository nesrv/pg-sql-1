
# Решения 

1. Соедините две таблицы `Orders` и `Customers` с помощью команды 'SELECT' (декартово произведение)
2. Соедините две таблицы `customers` и `orders` с помощью обычного 'JOIN'
3. Соедините две таблицы `customers` и `orders` с помощью 'LEFT JOIN'
4. Выведите покупателей, которые ничего не купили
5. Выведите ID товаров, которые не были проданы
6. Выведите название непроданных товаров

```sql
SELECT *
FROM Orders
JOIN Products ON
productid = Products.id;

SELECT productname
FROM orders
RIGHT JOIN customers ON
customers.id = orders.customerid
RIGHT JOIN products ON
products.id = productid
WHERE productid IS NULL;

```
