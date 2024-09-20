from passlib.context import CryptContext
from fastapi import HTTPException
from typing import Dict
from schemas.user import UserCreate

# Inicialización de contexto para hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Base de datos falsa de usuarios
fake_users_db = {}

# Registro de nuevo usuario
def register_user(user: UserCreate) -> Dict[str, str]:
    hashed_password = pwd_context.hash(user.password)
    fake_users_db[user.username] = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,
        "disabled": False,
    }
    return {"msg": "User created successfully"}


# Inicio de sesión de usuario
def login_user(username: str, password: str) -> Dict[str, str]:
    user = fake_users_db.get(username)
    
    # Verificar si el usuario existe y si la contraseña es correcta
    if not user or not pwd_context.verify(password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"msg": "Login successful"}
