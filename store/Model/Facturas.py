from sqlalchemy import Column, Float, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config.db import Base

class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String, nullable=False)  
    name = Column(String, nullable=False) 
    discount = Column(Float, default=0.0)  
    payment_status = Column(Boolean, default=False)  

    factura_products = relationship("FacturaProducts", back_populates="factura")



class FacturaProducts(Base):
    __tablename__ = "facturaProducts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    factura_id = Column(Integer, ForeignKey("facturas.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer,nullable=False,default=0)  

    factura = relationship("Factura", back_populates="factura_products")
    product = relationship("Product", back_populates="factura_products")
 
