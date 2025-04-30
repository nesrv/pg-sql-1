from sqlalchemy.orm import Session
from sqlalchemy import create_engine, not_, or_, select
from models import Product


engine = create_engine("postgresql://postgres:postgres@localhost:5434/bookstore")


with Session(engine) as session:
    cheap_products = session.query(Product).filter(Product.price < 40000).all()
    for product in cheap_products:
        print(product.productname, product.price)
    print(cheap_products)


with Session(engine) as session:
    stmt = select(Product).where(Product.price < 40000)
    cheap_products = session.execute(stmt).scalars().all()
    print(cheap_products)
    # for product in cheap_products:
    #     print(product.productname, product.price)


with Session(engine) as session:
    results = (
        session.query(Product)
        .filter(Product.company == "Samsung", Product.price > 50000)
        .all()
    )
    print(results)


with Session(engine) as session:
    stmt = (
        select(Product).where(Product.company == "Samsung").where(Product.price > 50000)
    )
    results = session.execute(stmt).scalars().all()
    print(results)


with Session(engine) as session:
    stmt = select(Product).where(
        or_(Product.company == "Samsung", Product.price > 50000)
    )
    results = session.execute(stmt).scalars().all()
    print(4, results)


with Session(engine) as session:
    stmt = select(Product).where(
        (Product.company == "Samsung") | (Product.price > 50000)
    )
    results = session.execute(stmt).scalars().all()
    print(5, results)

with Session(engine) as session:
    result = (
        session.query(Product)
        .filter((Product.company == "Samsung") | (Product.price > 50000))
        .all()
    )
    print(6, results)


with Session(engine) as session:
    stmt = select(Product).where(Product.company != 'Samsung')
    results = session.execute(stmt).scalars().all()
    print(7, results)
    # result = session.query(Product).filter(Product.company != "Samsung").all()
    # result = session.query(Product).filter(~(Product.company == 'Samsung')).all()
    # result = session.query(Product).filter_by(company='Samsung').filter(Product.company != 'Samsung').all()
    # print(7, results)

with Session(engine) as session:
    stmt = select(Product).where(not_(Product.company == 'Samsung'))
    results = session.execute(stmt).scalars().all()
    print(8, results)
    
    
with Session(engine) as session:
    results = session.query(Product).filter(Product.company != 'Samsung').all()
    print(9, results)
    

"""    
session.execute(stmt)

session - объект сессии SQLAlchemy, который управляет соединением с БД
stmt (statement) - SQL-запрос, построенный с помощью SQLAlchemy
execute() выполняет этот запрос в БД

.scalars()

Преобразует результат в скалярные значения (отдельные значения, а не целые строки)
Полезно, когда запрос возвращает только один столбец
Эквивалентно получению первого элемента каждой строки результата

.all()

Извлекает все строки результата сразу и возвращает их в виде списка
Альтернатива - использовать итерацию (например, в цикле for), если нужно обрабатывать результаты по одному
"""
