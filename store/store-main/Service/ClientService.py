from Repository.ClientRepository import ClientRepository
from Schemas.Schemas import Client as Client_Schemas

@staticmethod
def Get( connection): 
    reservationRepo = ClientRepository(connection)

    reservation = reservationRepo.Get()

    return reservation


@staticmethod
def Get_By_Id(connection,id:int ): 
    reservationRepo = ClientRepository(connection)    
    new_reservation = reservationRepo.Get_By_Id(id)
    return new_reservation

@staticmethod
def Post( connection,reservation_: Client_Schemas): 
    reservationRepo = ClientRepository(connection)    
    new_reservation = reservationRepo.Add(reservation_)
    return new_reservation

@staticmethod
def Put( connection,reservation_: Client_Schemas): 
    reservationRepo = ClientRepository(connection) 
    reservation_Update = reservationRepo.Update(reservation_)
    return reservation_Update

@staticmethod
def Delete(id:int, connection): 
    serviceRepo = ClientRepository(connection)
    serviceRepo.Get_By_Id(id)
    response = serviceRepo.Delete(id)
    return response