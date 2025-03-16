-- Случайным образом отберите 3 вопроса по дисциплине «Основы баз данных».
-- В результат включите столбцы question_id и name_question.

-- таблица question
--
-- +-------------+-------------------------------------------------------------------------+------------+
-- | question_id | name_question                                                           | subject_id |
-- +-------------+-------------------------------------------------------------------------+------------+
-- | 1           | Запрос на выборку начинается с ключевого слова:                         | 1          |
-- | 2           | Условие, по которому отбираются записи, задается после ключевого слова: | 1          |
-- | 3           | Для сортировки используется:                                            | 1          |
-- | 4           | Какой запрос выбирает все записи из таблицы student:                    | 1          |
-- | 5           | Для внутреннего соединения таблиц используется оператор:                | 1          |
-- | 6           | База данных - это:                                                      | 2          |
-- | 7           | Отношение - это:                                                        | 2          |
-- | 8           | Концептуальная модель используется для                                  | 2          |
-- | 9           | Какой тип данных не допустим в реляционной таблице?                     | 2          |
-- +-------------+-------------------------------------------------------------------------+------------+


CREATE TABLE IF NOT EXISTS question
(
    question_id   INT,
    name_question text,
    subject_id    INT
);



INSERT INTO question
VALUES (1, 'Запрос на выборку начинается с ключевого слова:', 1),
       (2, 'Условие, по которому отбираются записи, задается после ключевого слова:', 1),
       (3, 'Для сортировки используется:', 1),
       (4, 'Какой запрос выбирает все записи из таблицы student:', 1),
       (5, 'Для внутреннего соединения таблиц используется оператор:', 1),
       (6, 'База данных - это:', 2),
       (7, 'Отношение - это:', 2),
       (8, 'Концептуальная модель используется для:', 2),
       (9, 'Какой тип данных не допустим в реляционной таблице?', 2);


--solution-1

SELECT question_id,
       name_question
FROM question
WHERE subject_id = 1
ORDER BY RANDOM()
LIMIT 3;

--solution-2

SELECT question_id, name_question
FROM question
WHERE subject_id = (SELECT subject_id
                    FROM subject
                    WHERE name_subject = 'Основы баз данных')
ORDER BY RANDOM()
LIMIT 3;

--solution-3

SELECT question_id, name_question
FROM subject
         JOIN question USING (subject_id)
WHERE name_subject = 'Основы баз данных'
ORDER BY RANDOM()
LIMIT 3;

--solution-4

SELECT question_id, name_question
FROM subject
         INNER JOIN question USING (subject_id)
WHERE name_subject LIKE 'Основы баз данных'
ORDER BY RANDOM()
LIMIT 3;

--solution-5

SELECT question_id, name_question
FROM question q
         INNER JOIN subject s ON q.subject_id = s.subject_id AND name_subject = 'Основы баз данных'
ORDER BY RANDOM()
LIMIT 3;

--solution-6

SELECT question_id, name_question
FROM question
WHERE subject_id = (SELECT subject_id
                    FROM subject
                    WHERE name_subject LIKE 'Основы баз%')
ORDER BY RANDOM()
LIMIT 3







