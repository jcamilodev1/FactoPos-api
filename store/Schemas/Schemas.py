from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime

class Client(BaseModel):
    id: Optional[int] = None
    name: str= "Client_name"
    phone: str = "1234567890"
    birth_date: datetime = datetime.now().date()
    cc: Optional[str] = ""

class Client_post(BaseModel):
    name: str= "Client_name"
    phone: str = "1234567890"
    birth_date: Optional[datetime] = None  
    cc: Optional[str] = None  
    
class Client_post_Login(BaseModel):
    phone: str = "1234567890"
    cc: str = "00000000"


class Factura(BaseModel):
    id: Optional[int] = None
    phone: str = "1234567890"
    name: str = "Alex"
    discount: float = 0
    payment_status: bool = False

class Factura_Post(BaseModel):
    phone: str = "1234567890"
    name: str = "Alex"
    discount: float = 0
    payment_status: bool = False
    products:List[Dict[str,int]] = [
    {'product_id': 0,  'quantity': 1}    
]

class Factura_New(BaseModel):
    phone: str = "1234567890"
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



class Factura_Product(BaseModel):
    id: Optional[int] = None
    factura_id: int = 0
    product_id: int = 0


class Factura_Product_Post(BaseModel):
    factura_id: int = 0
    product_id: int = 0
    quantity: int = 0