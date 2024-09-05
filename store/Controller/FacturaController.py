from fastapi import APIRouter, Body, HTTPException
from fastapi import APIRouter, Body, HTTPException
from config.db import get_db
from Service.FactureService import FactureService

from Schemas.Schemas import Factura , Factura_Post
router = APIRouter()
@router.get("/")
async def Get():
    try: 
        Reservations =  FactureService.Get(get_db) 
        return Reservations
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        

@router.get("/{id}")
async def Get_By_Id(id:int):
        try:       
                reservaton_Byid = FactureService.Get_By_Id(get_db,id )
                return  reservaton_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))       

@router.post("/")
async def Post(
        queryBody: Factura_Post = Body(...)
        ):
        try:
                reservaton_Byid = FactureService.Post(get_db,queryBody )
                return  reservaton_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
        
@router.put("/")
async def Put(
        queryBody: Factura = Body(...)
        ):
        try:       
                new_reservation = FactureService.Put(get_db,queryBody )
                return  new_reservation
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}")
async def Delete(id:int):        
        response = FactureService.Delete(id ,get_db )
        return  response