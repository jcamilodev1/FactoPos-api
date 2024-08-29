from Repository.ProductRepository import ProductRepository
from Schemas.Schemas import Product as Prodyct_Schemas

@staticmethod
def Get( connection): 
    reservationRepo = ProductRepository(connection)

    reservation = reservationRepo.Get()

    return reservation


@staticmethod
def Get_By_Id(connection,id:int ): 
    reservationRepo = ProductRepository(connection)    
    new_reservation = reservationRepo.Get_By_Id(id)
    return new_reservation

@staticmethod
def Post( connection,reservation_: Prodyct_Schemas): 
    reservationRepo = ProductRepository(connection)    
    new_reservation = reservationRepo.Add(reservation_)
    return new_reservation

@staticmethod
def Put( connection,reservation_: Prodyct_Schemas): 
    reservationRepo = ProductRepository(connection) 
    reservation_Update = reservationRepo.Update(reservation_)
    return reservation_Update

@staticmethod
def Delete(id:int, connection): 
    serviceRepo = ProductRepository(connection)
    serviceRepo.Get_By_Id(id)
    response = serviceRepo.Delete(id)
    return response