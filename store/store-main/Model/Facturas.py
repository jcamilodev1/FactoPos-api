from sqlalchemy import Column, Float, Integer, String, Boolean
from config.db import Base

class Invoice(Base):
    __tablename__ = "Factura"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String, nullable=False)  
    name = Column(String, nullable=False) 
    discount = Column(Float, default=0.0)  
    payment_status = Column(Boolean, default=False)  
