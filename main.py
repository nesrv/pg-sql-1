from sqlalchemy import create_engine, func, desc, select
from sqlalchemy.orm import Session, joinedload, selectinload
from models import Attempt, Subject, Question, Answer, Testing


# DB = "postgresql://postgres:postgres@localhost/5433/bookstore"


DB = "postgresql://postgres:postgres@localhost:5433/testing_bd"
engine = create_engine(DB, echo=False)


## Для каждого вопроса вывести процент успешных решений,

# * то есть отношение количества верных ответов к общему количеству ответов,
# * значение округлить до 2-х знаков после запятой.
# * Также вывести название предмета, к которому относится вопрос,
# * и общее количество ответов на этот вопрос.
# * В результат включить название дисциплины, вопросы по ней (столбец назвать Вопрос),
# * а также два вычисляемых столбца Всего_ответов и Успешность.
# * Информацию отсортировать сначала по названию дисциплины, потом по убыванию успешности,
# * а потом по тексту вопроса в алфавитном порядке.
# * Поскольку тексты вопросов могут быть длинными, обрезать их 30 символов и добавить многоточие "...".

with Session(autoflush=False, bind=engine) as db:
    result = db.query(
        Subject.name_subject,
        Question.name_question,
        Question.question_id.label("Вопрос"),
        Answer.is_correct.label("Результат"))\
            .join(Question, Subject.subject_id == Question.subject_id)\
            .join(Answer, Question.question_id == Answer.question_id)\
            .order_by(
            Subject.name_subject,
            Answer.is_correct.desc(),
            Question.name_question.desc()
       
    ).all()
    print(*result, sep="\n")
    # query = select(Subject).options(joinedload(Question.name_question))
    # result = db.execute(query)
    # result = select(Subject).options(joinedload(Question).all())
    # print(*result, sep="\n")
