from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class Client(BaseModel):
    id: Optional[int] = None
    phone: str = "123-456-7890"
    birth_date: datetime = datetime.now().date()
    cc: str = "00000000"

class Client_post(BaseModel):
    phone: str = "123-456-7890"
    birth_date: datetime = datetime.now().date()
    cc: str = "00000000"

class Client_post_Login(BaseModel):
    phone: str = "123-456-7890"
    cc: str = "00000000"


class Factura(BaseModel):
    id: Optional[int] = None
    phone: str = "123-456-7890"
    name: str = "Alex"
    discount: float = 0
    payment_status: bool = False

class Factura_Post(BaseModel):
    id: Optional[int] = None
    phone: str = "123-456-7890"
    name: str = "Alex"
    discount: float = 0
    payment_status: bool = False


class Product(BaseModel):
    id: Optional[int] = None
    name: str = "Product_name"
    image: str = "Url"
    price: float = 0

class Product_Post(BaseModel):
    name: str = "Product_name"
    image: str = "Url"
    price: float = 0