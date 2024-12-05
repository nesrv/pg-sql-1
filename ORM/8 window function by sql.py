import sqlite3, psycopg2

# con = sqlite3.connect("ORM/books.db") # for sqlite
con = psycopg2.connect(dbname="books", user="postgres",
                        password="postgres", host="127.0.0.1", port="5432")


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
    SELECT *, round(CAST(float8  (price - avg_price) as numeric),2) as diff
        FROM (
        SELECT
            a.name_author,
            b.title,
            b.price,
            round(avg(b.price) over(PARTITION BY name_author)::numeric, 2) as avg_price
        FROM book b
        JOIN author a ON b.author_id = a.author_id) t1
)
SELECT * FROM t2
ORDER BY diff DESC;
'''

# cursor.execute(sql3)
# print(*cursor.fetchall(), sep='\n')


# sql4='''
# CREATE FUNCTION ROUND(float,int) RETURNS NUMERIC AS $f$
#   SELECT ROUND( CAST($1 AS numeric), $2 )
# $f$ language SQL IMMUTABLE;
# '''

sql5='''
CREATE or replace FUNCTION hello(name text) -- формальный параметр
RETURNS text
RETURN 'Hello, ' || name || '!';
'''
cursor.execute(sql5)
con.commit()
# print(cursor.callproc('hello', ['World']))