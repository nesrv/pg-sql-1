from sqlalchemy.orm import Session
from sqlalchemy import Float, create_engine, distinct, func, not_, or_, select
from models import Product


engine = create_engine("postgresql://postgres:postgres@localhost:5434/bookstore")

"""
1.  Найти минимальную цену товара в базе данных
2. Вывести товар с минимальной ценой
Найдем среднюю цену товаров из базы данных
2.  Найти среднюю цену для товаров конкретного производителя
3.  Найти среднюю сумму всех товаров, учитывая их количество:
4.  Найти минимальную, максимальную цену среди товаров, а также разницу между max и min
5*.  Получить названия продуктов с минимальной и максимальной ценой
5.  Посчитать общее количество товаров
6.  Узнать, есть ли в таблице товары, которые подлежать скидке, то есть у которых `IsDiscounted = true` (`BOOL_OR`)
7.  Узнать, все ли товары подлежат скидке `BOOL_AND`
8.  Выберести названия всех товаров через запятую (`STRING_AGG`)
9.  Выберести названия всех компаний через зап
"""

# Найти минимальную цену товара в базе данных
with Session(engine) as session:
    min_price = session.query(func.min(Product.price, type_=Float)).scalar()
    result = session.query(Product).filter(Product.price == min_price).first()
    print("1_мин_цена = ", result)
 
with Session(engine) as session:
    result = session.query(Product)\
        .order_by(Product.price)\
        .first()
    print("2_", result)
    if result:
        print(f"Продукт: {result.productname}")
        print(f"Цена: {result.price}")
        print(f"Компания: {result.company}")   



with Session(engine) as session:
    min_price = session.query(func.min(Product.price, type_=Float)).scalar()
    result = session.query(Product).filter(Product.price == min_price).first()
    print("1_мин_цена = ", result)


with Session(engine) as session:
    average_price = session.query(func.avg(Product.price, type_=Float)).scalar()
    # print(1, average_price)

with Session(engine) as session:
    average_price = session.execute(
        select(func.avg(Product.price).label("Average_Price"))
    ).scalar()
    # print(12, average_price)


with Session(engine) as session:
    result = (
        session.query(Product.company, func.avg(Product.price, type_=Float))
        .filter(Product.company == "Samsung")
        .group_by(Product.company)
        .first()
    )
    print(2, result)

with Session(engine) as session:
    result = (
        session.query(Product.company, func.avg(Product.price, type_=Float))
        .group_by(Product.company)
        .all()
    )
    print(20, result)


with Session(engine) as session:
    stmt = (
        select(Product.company, func.avg(Product.price).cast(Float))
        .where(Product.company == "Samsung")
        .group_by(Product.company)
    )
    result = session.execute(stmt).first()
    # print(21, result)


with Session(engine) as session:
    stmt = select(Product.company, func.avg(Product.price).cast(Float)).group_by(
        Product.company
    )
    result = session.execute(stmt).all()
    # print(22, result)


with Session(engine) as session:
    stmt = select(
        func.min(Product.price).cast(Float).label("min_price"),
        func.max(Product.price).cast(Float).label("max_price"),
        (func.max(Product.price) - func.min(Product.price))
        .cast(Float)
        .label("price_difference"),
    )
    result = session.execute(stmt).first()
    if result:
        min_price, max_price, price_diff = result
        print(f"Минимальная цена: {min_price}")
        print(f"Максимальная цена: {max_price}")
        print(f"Разница: {price_diff}")


with Session(engine) as session:
    result = session.query(
        func.min(Product.price).cast(Float).label("min_price"),
        func.max(Product.price).cast(Float).label("max_price"),
        (func.max(Product.price) - func.min(Product.price))
        .cast(Float)
        .label("price_difference"),
    ).first()
    if result:
        min_price, max_price, price_diff = result
        print(f"Минимальная цена: {min_price}")
        print(f"Максимальная цена: {max_price}")
        print(f"Разница: {price_diff}")


# SQLAlchemy 2.0
# with Session(engine) as session:
#     # Находим мин и макс цены
#     subq = (
#         select(
#             func.min(Product.price).label('min_price'),
#             func.max(Product.price).label('max_price')
#         )
#     ).scalar_subquery()

#     # Находим продукты с этими ценами
#     stmt = (
#         select(
#             Product.productname,
#             Product.price,
#             Product.company
#         )
#         .where(
#             or_(
#                 Product.price == subq.c.min_price,
#                 Product.price == subq.c.max_price
#             )
#         )
#     )

#     results = session.execute(stmt).all()
#     for name, price, company in results:
#         print(f"Продукт: {name}, Цена: {price}, Компания: {company}")
