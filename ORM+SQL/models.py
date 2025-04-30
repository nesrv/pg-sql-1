from sqlalchemy import  Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base


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
