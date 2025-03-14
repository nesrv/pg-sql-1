-- Студенты могут тестироваться по одной или нескольким дисциплинам (не обязательно по всем).
-- Вывести дисциплину и количество уникальных студентов (столбец назвать Количество),
-- которые по ней проходили тестирование .
-- Информацию отсортировать сначала по убыванию количества, а потом по названию дисциплины.
-- В результат включить и дисциплины, тестирование по которым студенты еще не проходили,
-- в этом случае указать количество студентов 0.


--solution-1 left join

SELECT name_subject, COUNT(DISTINCT student_id) AS Количество
FROM subject s
         LEFT JOIN attempt a USING (subject_id)
GROUP BY name_subject
ORDER BY 2 DESC, 1;

--solution-2 rigth join

SELECT name_subject, COUNT(DISTINCT(student_id)) Количество
FROM attempt RIGHT JOIN subject USING(subject_id)
GROUP BY 1 ORDER BY 2 DESC, 1;

--solution-3

SELECT name_subject,
       COUNT(query_in.student_id) AS Количество
FROM (SELECT DISTINCT subject_id, student_id FROM attempt) query_in
         RIGHT JOIN subject
                    ON query_in.subject_id = subject.subject_id
GROUP BY name_subject
ORDER BY Количество DESC, name_subject;

--solution-3

SELECT name_subject, COUNT(DISTINCT student_id) AS Количество
FROM subject
         LEFT JOIN attempt USING (subject_id)
GROUP BY name_subject
ORDER BY 2 DESC, 1;