from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import select
from sqlalchemy.orm import Session


Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'  # Название таблицы в БД

    id = Column(Integer, primary_key=True, autoincrement=True)  # SERIAL в PostgreSQL
    productname = Column(String(30), nullable=False)  # VARCHAR(30) NOT NULL
    company = Column(String(20), nullable=False)      # VARCHAR(20) NOT NULL
    productcount = Column(Integer, default=0)        # INTEGER DEFAULT 0
    price = Column(Numeric)                          # NUMERIC
    
    def __repr__(self):
        return f"<Product(Id={self.id}, Name='{self.productname}', Price={self.price})>"

# Подключение к БД

engine = create_engine("postgresql://postgres:postgres@localhost:5434/bookstore")
# Session = sessionmaker(bind=engine)
# session = Session()

# # Запрос
# cheap_products = session.query(Product).filter(Product.price < 40000).all()
# print(cheap_products)



with Session(engine) as session:
    stmt = select(Product).where(Product.price < 40000)
    cheap_products = session.execute(stmt).scalars().all()
    for product in cheap_products:
        print(product.productname, product.price)