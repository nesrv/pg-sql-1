from sqlalchemy.orm import Session
from sqlalchemy import create_engine, distinct, not_, or_, select
from models import Product


engine = create_engine("postgresql://postgres:postgres@localhost:5434/bookstore")
"""
1.  Вывести всех производителей
2.  Вывести сумму товарных запасов, отсортированную по убыванию
3.  Вывести первые 2 строки таблицы
4.  Вывести 3 строки таблицы, начиная с 2-й
5.  Вывести все строки таблицы после второй

"""


with Session(engine) as session:
    query = select(distinct(Product.company))
    result = session.execute(query).scalars().all()
    # print(1, result)


with Session(engine) as session:
    query = select(Product.company).group_by(Product.company)
    result = session.execute(query).scalars().all()
    # print(12, result)


with Session(engine) as session:
    result = session.query(distinct(Product.company)).all()
    # print(13, result)
    result = session.query(Product.company).distinct().all()
    # print(14, result)


with Session(engine) as session:
    query = session.query(
        Product.productname, (Product.productcount * Product.price).label("TotalSum")
    ).order_by("TotalSum")

    # Выполняем запрос
    result = query.all()
    # print(2, *result, sep="\n")


with Session(engine) as session:
    result = session.query(Product).order_by(Product.productname).limit(2).all()

    print(3, *result, sep="\n")


with Session(engine) as session:
    result = (
        session.query(Product).order_by(Product.productname).offset(2).limit(3).all()
    )
    # print(4, *result, sep="\n")


with Session(engine) as session:
    stmt = select(Product).offset(2).limit(3)
    result = session.execute(stmt).scalars().all()
    # print(41, *result, sep="\n")


with Session(engine) as session:
    stmt = select(Product).offset(2)
    result = session.execute(stmt).scalars().all()
    print(5, *result, sep="\n")

with Session(engine) as session:
    stmt = select(Product).offset(2).limit(None)  # эквивалент LIMIT ALL
    result = session.execute(stmt).scalars().all()
    print(51, *result, sep="\n")

with Session(engine) as session:
    result = session.query(Product) \
        .offset(2) \
        .all()
    print(52, *result, sep="\n")
