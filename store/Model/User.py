from sqlalchemy import Column, Integer, String, Date, Boolean
from config.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, default="Client_name")
    phone = Column(String, nullable=False, default="1234567890")
    birth_date = Column(Date, nullable=True)
    cc = Column(String, nullable=True)
    cc_type = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email = Column(String, nullable=True)
    name_business = Column(String, nullable=False, default="1234567890")
    phone_business = Column(String, nullable=False, default="1234567890")
    cc_business = Column(String, nullable=True)
    cc_type_business = Column(String, nullable=True)
    number_employees = Column(Integer, nullable=True)
    password = Column(String, nullable=False)
