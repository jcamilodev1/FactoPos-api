from fastapi import APIRouter, Body, HTTPException
from config.db import get_db
from Service.ClientService import Client_Service
from Schemas.Schemas import Client_post , Client, Client_post_Login
router = APIRouter()
@router.get("/")
async def Get():
    try: 
        Reservations =  Client_Service.Get(get_db) 
        return Reservations
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        

@router.get("/{id}")
async def Get_By_Id(id:int):
        try:       
                reservaton_Byid = Client_Service.Get_By_Id(get_db,id )
                return  reservaton_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))   

@router.get("Phone/{num}")
async def Get_By_Phone(num:int):
        try:       
                Phone_Byid = Client_Service.Get_By_Phone(get_db,num )
                return  Phone_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))    

@router.post("/")
async def Post(
        queryBody: Client_post = Body(...)
        ):
        try:
                reservaton_Byid = Client_Service.Post(get_db,queryBody )
                return  reservaton_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
        
@router.post("/Login")
async def Post(
        queryBody: Client_post_Login = Body(...)
        ):
        try:
                reservaton_Byid = Client_Service.Login(get_db,queryBody )
                return  reservaton_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
        
@router.put("/")
async def Put(
        queryBody: Client = Body(...)
        ):
        try:       
                new_reservation = Client_Service.Put(get_db,queryBody )
                return  new_reservation
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}")
async def Delete(id:int):        
        response = Client_Service.Delete(id ,get_db )
        return  response
