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