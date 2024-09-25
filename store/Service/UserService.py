from Repository.UserRepository import UserRepository
from Schemas.Schemas import User , LoginSchema


class UserService:

    def Post(connection, user_: User): 
        user_repo = UserRepository(connection)  
        return user_repo.create_user_oauth(user_)

    def GetUser(connection, user_: LoginSchema):
        user_repo = UserRepository(connection)  
        return user_repo.login(user_)