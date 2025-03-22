# Задание

Вывести студентов, которые сдавали дисциплину «Основы баз данных», указать дату попытки и результат.
Информацию вывести по убыванию результатов тестирования.

Результат

| name_student    | date_attempt | result |
| --------------- | ------------ | ------ |
| Яковлева Галина | 2020-04-21   | 100    |
| Баранов Павел   | 2020-03-23   | 67     |
| Яковлева Галина | 2020-03-26   | 0      |

```sql
select name_student,date_attempt,result
    from student
    join attempt using (student_id)
    join subject using (subject_id)
where name_subject = "Основы баз данных"
order by 3 desc;
```

```py
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from models import *

# DB = "postgresql://postgres:postgres@localhost/5433/bookstore"
DB = "postgresql://postgres:postgres@localhost:5433/testing_bd"
engine = create_engine(DB, echo=True)

# check bd
with Session(autoflush=False, bind=engine) as db:
    student = db.query(Student).all()
    for st in student:
        print(st)


# solution-1

with Session(autoflush=False, bind=engine) as db:
    students = (
        db.query(Student)
        .join(Attempt)  
        .join(Subject, Attempt.subject_id == Subject.subject_id)  
        .filter(Subject.name_subject == "Основы баз данных")
        .order_by(Attempt.result.desc())
        .all()
    )
    print(*students)

# solution-2
with Session(autoflush=False, bind=engine) as db:
    query = db.query(Student)   
    query = query.join(Attempt).join(Subject,Attempt.subject_id == Subject.subject_id) 
    query = query.filter(Subject.name_subject == "Основы баз данных")    
    query = query.order_by(Attempt.result.desc())
    students = query.all()
    print(*students)
```
