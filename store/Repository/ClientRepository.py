from fastapi import HTTPException
from sqlalchemy import select,insert,delete, update , and_, or_, func
from Model.Clients import Customer as Customer_Model
from Schemas.Schemas import Client as customer_Schemas, Client_post_Login
class ClientRepository:
    
    def __init__(self, connection):
        self.connection = connection


    def Get(self):
        query = select(Customer_Model)
        result = self.connection.execute(query).fetchall()
        reservation_List = [dict(row._mapping) for row in result]
        return reservation_List
    
    def Get_By_Id(self, id: int):
        query = select(Customer_Model).where(Customer_Model.id == id)
        result = self.connection.execute(query).fetchone()

        if(result is None):
            raise HTTPException(status_code=404, detail="No client found")   
           
        service_result = dict(result._mapping)
        return service_result
    
    def Get_By_Phone(self, phone: str):
        query = select(Customer_Model).where(Customer_Model.phone == phone)
        result = self.connection.execute(query).fetchone()

        if(result is None):
            return None   
           
        service_result = dict(result._mapping)
        return service_result
    
    def Get_By_cc(self, cc: str):
        query = select(Customer_Model).where(Customer_Model.cc == cc
                                         or  Customer_Model.phone == cc )
        result = self.connection.execute(query).fetchone()

        if(result is  None):          
            return None
       
        service_result = dict(result._mapping)
        return service_result
    
    def Add(self, client_:customer_Schemas ):
        client__data = client_.dict()
        query = insert(Customer_Model).values(client__data)
        self.connection.execute(query)
        self.connection.commit()
        return "Added new client"
    
    def Login(self, Reservation_:customer_Schemas ):
        service_data = Reservation_.dict()
        query = insert(Customer_Model).values(service_data)
        self.connection.execute(query)
        self.connection.commit()
        return "Added new client"
    
    def Update(self, reservation_:customer_Schemas ):
        service_data = reservation_.dict()
        query = update(Customer_Model).where(Customer_Model.id == reservation_.id).values(service_data)
        self.connection.execute(query)
        self.connection.commit()
        return "Update reservation"

    
    def Delete(self, id: int ):

        query = delete(Customer_Model).where(Customer_Model.id == id)
        self.connection.execute(query)
        self.connection.commit()
        return "Reservation was delete"
