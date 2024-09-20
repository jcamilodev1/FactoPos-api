from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserLogin
from services.user_service import register_user, login_user

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    result = register_user(user)
    if not result:
        raise HTTPException(status_code=400, detail="Registration failed")
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: UserLogin):
    token = login_user(user.username, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
