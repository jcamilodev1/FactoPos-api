from fastapi import APIRouter, Body, HTTPException
from fastapi import APIRouter, Body, HTTPException
from config.db import get_db
from Service.UserService import UserService

from Schemas.Schemas import LoginSchema , User
router = APIRouter()

@router.post("/")
async def Post(
        queryBody: User = Body(...)
        ):
        try:
                user_Byid = UserService.Post(get_db,queryBody )
                return  user_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
        

@router.post("/login")
async def Post(
        queryBody: LoginSchema = Body(...)
        ):
        try:
                user_Byid = UserService.GetUser(get_db,queryBody )
                return  user_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
