from Repository.FacturaRepository import FacturaRepository
from Service import ClientService , FacturaProductsService
from Schemas.Schemas import Factura as factura_Schemas , Factura_Post, Client_post, Factura_New , Factura_Product_Post
from datetime import datetime

@staticmethod
def Get( connection): 
    reservationRepo = FacturaRepository(connection)

    reservation = reservationRepo.Get()

    return reservation


@staticmethod
def Get_By_Id(connection,id:int ): 
    reservationRepo = FacturaRepository(connection)    
    new_reservation = reservationRepo.Get_By_Id(id)
    return new_reservation

@staticmethod
def Post( connection,factura_: Factura_Post):
    # cliente existe 
    client = ClientService.Get_By_Phone(connection, factura_.phone )
    if(  len(client) == 0 ):
        # Crear cliente
        new_client =  Client_post(name=factura_.name, phone=factura_.phone , birth_date=None, cc=None)
        ClientService.Post(connection, new_client)
    # Crear una nueva factura
    new_factura =  Factura_New(phone=factura_.phone, name=factura_.name, discount=factura_.discount, payment_status=factura_.payment_status)
    FacturaRepo = FacturaRepository(connection)    
    Factura_id = FacturaRepo.Add(new_factura)
    # añadir los productos
    for p in factura_.products:
        Data_factura_products = Factura_Product_Post(factura_id=Factura_id, product_id= p['product_id'], quantity=p['quantity'] )
        FacturaProductsService.Post(connection, Data_factura_products)
    
    return "factura fue creada"

@staticmethod
def Put( connection,reservation_: factura_Schemas): 
    reservationRepo = FacturaRepository(connection) 
    reservation_Update = reservationRepo.Update(reservation_)
    return reservation_Update

@staticmethod
def Delete(id:int, connection): 
    serviceRepo = FacturaRepository(connection)
    serviceRepo.Get_By_Id(id)
    response = serviceRepo.Delete(id)
    return response