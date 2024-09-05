from Repository.ClientRepository import ClientRepository
from Schemas.Schemas import Client as Client_Schemas , Client_post
from datetime import datetime
class Client_Service:
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
    def Get_By_Phone(connection,phone:int ): 
        reservationRepo = ClientRepository(connection)    
        client = reservationRepo.Get_By_Phone(phone)
        return client



    @staticmethod
    def Post( connection,client_: Client_post): 
        reservationRepo = ClientRepository(connection)    
        new_reservation = reservationRepo.Add(client_)
        return new_reservation

    @staticmethod
    def Login( connection,client_Login: Client_Schemas): 
        reservationRepo = ClientRepository(connection)    
        # verificar que el usuario no exite
        user = reservationRepo.Get_By_cc(client_Login.cc)
        if(user):

            return "Usuario existe"
        else:
            reservationRepo.Add(client_Login)
            return "Usuario no existe, se creado nuevo usuario"
        new_reservation = reservationRepo.Login(client_Login)
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