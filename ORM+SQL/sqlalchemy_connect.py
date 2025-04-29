
from sqlalchemy import select
from sqlalchemy.orm import Session

with Session(engine) as session:
    stmt = select(Product).where(Product.price < 40000)
    cheap_products = session.execute(stmt).scalars().all()
    for product in cheap_products:
        print(product.name, product.price)