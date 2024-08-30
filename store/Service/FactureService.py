from Repository.FacturaRepository import FacturaRepository
from Service import ClientService
from Schemas.Schemas import Factura as factura_Schemas , Factura_Post, Client_post
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
    len(client)
    print(client)
    if(  len(client) == 0 ):
        new_client =  Client_post(name=factura_.name, phone=factura_.phone , birth_date=None, cc=None)
        ClientService.Post(connection, new_client)

    reservationRepo = FacturaRepository(connection)    
    new_reservation = reservationRepo.Add(factura_)
    return new_reservation

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