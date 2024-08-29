from sqlalchemy import Column, Float, Integer, String
from config.db import Base

class Product(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True, autoincrement=True) 
    name = Column(String, nullable=False) 
    image = Column(String, nullable=True)  
    price = Column(Float, nullable=False)  
