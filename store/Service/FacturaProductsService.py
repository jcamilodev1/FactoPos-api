from Repository.FacturaProductsRepository import FacturaProductsRepository
from Schemas.Schemas import Factura_Product_Post , Factura_Product
from Service import  ProductService , FactureService

@staticmethod
def Get( connection): 
    reservationRepo = FacturaProductsRepository(connection)
    reservation = reservationRepo.Get()

    return reservation


@staticmethod
def Get_By_Id(connection,id:int ): 
    reservationRepo = FacturaProductsRepository(connection)    
    new_reservation = reservationRepo.Get_By_Id(id)
    return new_reservation

@staticmethod
def Post( connection,factura: Factura_Product_Post): 
    FactureService.Get_By_Id(connection,factura.factura_id)
    ProductService.Get_By_Id(connection,factura.product_id)
    reservationRepo = FacturaProductsRepository(connection)    
    new_reservation = reservationRepo.Add(factura)
    return new_reservation

@staticmethod
def Put( connection,reservation_: Factura_Product): 
    reservationRepo = FacturaProductsRepository(connection) 
    reservation_Update = reservationRepo.Update(reservation_)
    return reservation_Update

@staticmethod
def Delete(id:int, connection): 
    serviceRepo = FacturaProductsRepository(connection)
    serviceRepo.Get_By_Id(id)
    response = serviceRepo.Delete(id)
    return response