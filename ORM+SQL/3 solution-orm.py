from sqlalchemy.orm import Session
from sqlalchemy import Float, create_engine, distinct, func, not_, or_, select
from models import Product


engine = create_engine("postgresql://postgres:postgres@localhost:5434/bookstore")

"""
1.  Найдем среднюю цену товаров из базы данных
2.  Найти среднюю цену для товаров определенного производителя
3.  Найти среднюю сумму всех товаров, учитывая их количество:
4.  Найти минимальную, максимальную цену среди товаров, а также разницу между max и min
5.  Посчитать общее количество товаров
6.  Узнать, есть ли в таблице товары, которые подлежать скидке, то есть у которых `IsDiscounted = true` (`BOOL_OR`)
7.  Узнать, все ли товары подлежат скидке `BOOL_AND`
8.  Выберести названия всех товаров через запятую (`STRING_AGG`)
9.  Выберести названия всех компаний через зап
"""


with Session(engine) as session:
    average_price = session.query(func.avg(Product.price, type_=Float)).scalar()
    # print(1, average_price)

with Session(engine) as session:
    average_price = session.execute(
        select(func.avg(Product.price).label("Average_Price"))
    ).scalar()
    # print(12, average_price)


with Session(engine) as session:
    result = session.query(
        Product.company,
        func.avg(Product.price, type_=Float)
    ).filter(
        Product.company == "Samsung"
    ).group_by(Product.company).first()
    print(2, result)

with Session(engine) as session:
    result = session.query(
        Product.company,
        func.avg(Product.price, type_=Float)   
    ).group_by(Product.company).all()
    print(20, result)


with Session(engine) as session:
    stmt = (
        select(
            Product.company,
            func.avg(Product.price).cast(Float)
        )
        .where(Product.company == "Samsung")
        .group_by(Product.company)
    )
    result = session.execute(stmt).first()
    print(21, result)


with Session(engine) as session:
    stmt = (
        select(
            Product.company,
            func.avg(Product.price).cast(Float)
        )        
        .group_by(Product.company)
    )
    result = session.execute(stmt).all()
    print(22, result)


