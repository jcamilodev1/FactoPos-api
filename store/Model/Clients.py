from sqlalchemy import Column, Integer, String, Date
from config.db import Base

class Customer(Base):
    __tablename__ = "Clients"  

    id = Column(Integer, primary_key=True, autoincrement=True)  
    name = Column(String, nullable=False)  
    phone = Column(String, nullable=False)  
    birth_date = Column(Date, nullable=True) 
    cc = Column(String, unique=True, nullable=True)  
