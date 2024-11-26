-- task 1

SELECT name, city, per_diem, date_first, date_last
FROM trip
-- WHERE name LIKE '%а ____'
WHERE name LIKE '%а %'
ORDER BY date_first DESC;


-- task 2
SELECT name
FROM trip
WHERE city = 'Москва'
GROUP BY name;
ORDER BY name;


-- task 3


SELECT city, COUNT(city) as Количество
from trip
GROUP BY city
ORDER BY city;

-- task 4

SELECT *
FROM trip
ORDER BY  date_first
LIMIT 1;

-- task 5

SELECT city, COUNT(city) as Количество
from trip
GROUP BY city
ORDER BY Количество DESC
LIMIT 2;

-- task 6
SELECT name, city, date_last - date_first + 1  as Длительность
FROM trip
WHERE city not in ('Москва', 'Санкт-Петербург')
ORDER BY Длительность DESC, city DESC;

-- task 7
SELECT name, city, date_first, date_last
FROM trip
WHERE date_last - date_first  = (SELECT MIN(date_last - date_first) FROM trip );

-- task 8
SELECT name, city, date_first, date_last
FROM trip
WHERE EXTRACT(MONTH FROM  date_first) = EXTRACT(MONTH FROM  date_last)
ORDER BY city, name;

-- task 9
SELECT to_char(date_first, 'Month') as Месяц, count(date_first) as Количество
FROM trip
GROUP BY Месяц
ORDER BY Количество DESC, Месяц;

-- task 10
SELECT  name, city, date_first, (date_last - date_first ) * per_diem  as Сумма
FROM trip
WHERE EXTRACT(MONTH FROM  date_first) BETWEEN 2 and 3
ORDER BY name, Сумма DESC; 

-- task 11

SELECT name, SUM((date_last- date_first) * per_diem) AS Сумма
FROM trip
GROUP by name
HAVING count(name) > 3
ORDER by 2 desc;