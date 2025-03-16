-- Если студент совершал несколько попыток по одной и той же дисциплине,
-- то вывести разницу в днях между первой и последней попыткой.
-- В результат включить фамилию и имя студента, название дисциплины и вычисляемый столбец Интервал.
-- Информацию вывести по возрастанию разницы. Студентов, сделавших одну попытку по дисциплине, не учитывать.



--add-table-subject
DROP TABLE IF EXISTS subject CASCADE;
CREATE TABLE IF NOT EXISTS subject
(
    subject_id   INT,
    name_subject text
);



INSERT INTO subject
VALUES (1, 'Основы SQL'),
       (2, 'Основы баз данных'),
       (3, 'Физика');


--solution-1

SELECT name_student,
       name_subject,
       EXTRACT(DAY FROM AGE(MAX(date_attempt), MIN(date_attempt)))::INTEGER AS interval_days
FROM student
         JOIN attempt USING (student_id)
         JOIN subject USING (subject_id)
GROUP BY name_student, name_subject
HAVING EXTRACT(DAY FROM AGE(MAX(date_attempt), MIN(date_attempt)))::INTEGER > 0
ORDER BY interval_days;

--solution-2

SELECT name_student, name_subject,
EXTRACT(DAY FROM AGE(MAX(date_attempt), MIN(date_attempt)))::INTEGER as Интервал
FROM student JOIN attempt USING (student_id)
             JOIN subject USING (subject_id)
GROUP BY name_student, name_subject
HAVING COUNT(date_attempt) > 1
ORDER BY Интервал;