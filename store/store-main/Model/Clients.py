from sqlalchemy import Column, Integer, String, Date
from config.db import Base

class Customer(Base):
    __tablename__ = "Clients"  

    id = Column(Integer, primary_key=True, autoincrement=True)  
    phone = Column(String, nullable=False)  
    birth_date = Column(Date, nullable=False) 
    cc = Column(String, unique=True, nullable=False)  
