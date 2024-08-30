from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    image = Column(String, nullable=True)
    price = Column(Float, nullable=False)

    factura_products = relationship("FacturaProducts", back_populates="product")
