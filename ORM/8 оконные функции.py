import sqlite3

con = sqlite3.connect("ORM/books.db")


cursor = con.cursor()

#оконная функция

sql1 = '''
SELECT
    a.name_author,
    b.title,
    b.price,
    avg(b.price) over(PARTITION BY name_author) as avg_price
FROM book b
JOIN author a ON b.author_id = a.author_id
'''
# cursor.execute(sql1)
# print(*cursor.fetchall(), sep='\n')


sql2 = '''
SELECT *, price - avg_price as diff
    FROM (
    SELECT
        a.name_author,
        b.title,
        b.price,
        avg(b.price) over(PARTITION BY name_author) as avg_price
    FROM book b
    JOIN author a ON b.author_id = a.author_id) t1
'''

# cursor.execute(sql2)
# print(*cursor.fetchall(), sep='\n')

sql3 = '''
WITH t2 AS (
    SELECT *, price - avg_price as diff
        FROM (
        SELECT
            a.name_author,
            b.title,
            b.price,
            avg(b.price) over(PARTITION BY name_author) as avg_price
        FROM book b
        JOIN author a ON b.author_id = a.author_id) t1
)
'''

cursor.execute(sql3)
print(*cursor.fetchall(), sep='\n')
