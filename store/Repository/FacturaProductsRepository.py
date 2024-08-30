from fastapi import HTTPException
from sqlalchemy import select,insert,delete, update , and_, or_, func
from Model.Facturas import  FacturaProducts  as Facture_Product_Model
from Schemas.Schemas import Product as product_Schemas
class FacturaProductsRepository:
    
    def __init__(self, connection):
        self.connection = connection


    def Get(self):
        query = select(Facture_Product_Model)
        result = self.connection.execute(query).fetchall()
        reservation_List = [dict(row._mapping) for row in result]
        return reservation_List
    
    def Get_By_Id(self, id: int):
        query = select(Facture_Product_Model).where(Facture_Product_Model.id == id)
        result = self.connection.execute(query).fetchone()

        if(result is None):
            raise HTTPException(status_code=404, detail="No product found")   
           
        service_result = dict(result._mapping)
        return service_result
    
    def Add(self, Reservation_:product_Schemas ):
        service_data = Reservation_.dict()
        query = insert(Facture_Product_Model).values(service_data)
        self.connection.execute(query)
        self.connection.commit()
        return "Added new FactureProduct"
    
    def Update(self, reservation_:product_Schemas ):
        service_data = reservation_.dict()
        query = update(Facture_Product_Model).where(Facture_Product_Model.id == reservation_.id).values(service_data)
        self.connection.execute(query)
        self.connection.commit()
        return "Update FactureProduct"

    
    def Delete(self, id: int ):

        query = delete(Facture_Product_Model).where(Facture_Product_Model.id == id)
        self.connection.execute(query)
        self.connection.commit()
        return "FactureProduct was delete"