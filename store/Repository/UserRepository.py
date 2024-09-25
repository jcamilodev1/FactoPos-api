from fastapi import HTTPException
from sqlalchemy import select, insert, delete, update, and_, or_, func
from Model.User import User as User_Model
import jwt
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError
from authlib.integrations.starlette_client import OAuth
from passlib.context import CryptContext
from sqlalchemy.orm import Session

SECRET_KEY = "2nc6Ek7KZDhT"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class UserRepository:
    def __init__(self, connection):
        self.connection = connection
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str):
        return self.pwd_context.hash(password)

    def create_user_oauth(self, oauth_data):
        try:
            user_dict = oauth_data.dict()
            user_dict['password'] = self.hash_password(user_dict['password'])  # Hashea la contraseña
            query = insert(User_Model).values(user_dict)

            result = self.connection.execute(query)
            self.connection.commit()

            user_id = result.inserted_primary_key[0]

            token = self.create_jwt_token(user_id, user_dict['email'])

            return {"access_token": token, "token_type": "bearer"}
        
        except SQLAlchemyError as e:
            self.connection.rollback()
            print("Database error in create_user_oauth:", str(e))
            raise HTTPException(status_code=500, detail="Error creating user")

    def create_jwt_token(self, user_id: int, email: str):
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        payload = {
            "sub": user_id,
            "email": email,
            "exp": expire
        }
        
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return token
    
    def login(self, login_data):
        try:
            query = select(User_Model).where(User_Model.email == login_data.email)
            result = self.connection.execute(query)
            user = result.fetchone()
            
            if user is None:
                raise HTTPException(status_code=401, detail="Invalid email or password")
            
            user = User_Model(**user._mapping)
            print("User fetched:", user)
            print("User type:", type(user))
            print("User attributes:", dir(user))
            print("Stored password hash:", user.password)

            try:
                is_valid = self.pwd_context.verify(login_data.password, user.password)
                print("Password verification result:", is_valid)
                
                if is_valid:
                    token = self.create_jwt_token(user.id, user.email)
                    return {"access_token": token, "token_type": "bearer"}
                else:
                    raise HTTPException(status_code=401, detail="Invalid email or password")
            except ValueError as ve:
                print("Password verification error:", str(ve))
                raise HTTPException(status_code=500, detail="Error verifying password")

        except SQLAlchemyError as e:
            print("Database error in login:", str(e))
            raise HTTPException(status_code=500, detail="Database error")
        except Exception as e:
            print("Unexpected error in login:", str(e))
            raise HTTPException(status_code=500, detail="Internal server error")


    def get_user_by_id(self, user_id: int):
        try:
            query = select(User_Model).where(User_Model.id == user_id)
            result = self.connection.execute(query)
            user = result.fetchone()
            
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            
            return User_Model(**user._mapping)
        except SQLAlchemyError as e:
            print("Database error in get_user_by_id:", str(e))
            raise HTTPException(status_code=500, detail="Database error")

    def update_user(self, user_id: int, user_data):
        try:
            query = update(User_Model).where(User_Model.id == user_id).values(**user_data.dict(exclude_unset=True))
            result = self.connection.execute(query)
            self.connection.commit()
            
            if result.rowcount == 0:
                raise HTTPException(status_code=404, detail="User not found")
            
            return {"message": "User updated successfully"}
        except SQLAlchemyError as e:
            self.connection.rollback()
            print("Database error in update_user:", str(e))
            raise HTTPException(status_code=500, detail="Error updating user")

    def delete_user(self, user_id: int):
        try:
            query = delete(User_Model).where(User_Model.id == user_id)
            result = self.connection.execute(query)
            self.connection.commit()
            
            if result.rowcount == 0:
                raise HTTPException(status_code=404, detail="User not found")
            
            return {"message": "User deleted successfully"}
        except SQLAlchemyError as e:
            self.connection.rollback()
            print("Database error in delete_user:", str(e))
            raise HTTPException(status_code=500, detail="Error deleting user")