from fastapi import HTTPException
from sqlalchemy import select,insert,delete, update , and_, or_, func
from Model.Facturas import Invoice   as Factura_Model
from Schemas.Schemas import Factura as factura_Schemas
class FacturaRepository:
    
    def __init__(self, connection):
        self.connection = connection


    def Get(self):
        query = select(Factura_Model)
        result = self.connection.execute(query).fetchall()
        reservation_List = [dict(row._mapping) for row in result]
        return reservation_List
    
    def Get_By_Id(self, id: int):
        query = select(Factura_Model).where(Factura_Model.id == id)
        result = self.connection.execute(query).fetchone()

        if(result is None):
            raise HTTPException(status_code=404, detail="No factura found")   
           
        service_result = dict(result._mapping)
        return service_result
    
    def Add(self, Reservation_:factura_Schemas ):
        service_data = Reservation_.dict()
        query = insert(Factura_Model).values(service_data)
        self.connection.execute(query)
        self.connection.commit()
        return "Added new factura"
    
    def Update(self, reservation_:factura_Schemas ):
        service_data = reservation_.dict()
        query = update(Factura_Model).where(Factura_Model.id == reservation_.id).values(service_data)
        self.connection.execute(query)
        self.connection.commit()
        return "Update factura"

    
    def Delete(self, id: int ):

        query = delete(Factura_Model).where(Factura_Model.id == id)
        self.connection.execute(query)
        self.connection.commit()
        return "Factura was delete"
