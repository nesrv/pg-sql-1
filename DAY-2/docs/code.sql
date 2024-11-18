```sql
INSERT INTO book (title, author, price, amount)
VALUES
    ('Белая гвардия', 'Булгаков М.А.', 540.50 , 5),
    ('Идиот', 'Достоевский Ф.М.', 460, 10),
    ('Братья Карамазовы', 'Достоевский Ф.М.', 799.01, 2);
```



SELECT title AS Название, author AS Автор
FROM book;

-- 8

SELECT title, amount, 
     1.65 * amount AS pack 
FROM book;


-- 10

SELECT title, author, amount, 
    ROUND(price * 0.7,2) AS new_price
FROM book;

-- 12

SELECT author, title,    
    ROUND(IF(author = "Булгаков М.А.", price * 1.1, IF (author = "Есенин С.А.", price * 1.05, price)),2) AS new_price
FROM book;