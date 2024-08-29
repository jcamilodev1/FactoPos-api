from fastapi import APIRouter, Body, HTTPException
from fastapi import APIRouter, Body, HTTPException
from config.db import get_db
from Service import FactureService as Facture_Service
from Schemas.Schemas import Factura , Factura_Post
router = APIRouter()
@router.get("/")
async def Get():
    try: 
        Reservations =  Facture_Service.Get(get_db) 
        return Reservations
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        

@router.get("/{id}")
async def Get_By_Id(id:int):
        try:       
                reservaton_Byid = Facture_Service.Get_By_Id(get_db,id )
                return  reservaton_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))       

@router.post("/")
async def Post(
        queryBody: Factura_Post = Body(...)
        ):
        try:
                reservaton_Byid = Facture_Service.Post(get_db,queryBody )
                return  reservaton_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
        
@router.put("/")
async def Put(
        queryBody: Factura = Body(...)
        ):
        try:       
                new_reservation = Facture_Service.Put(get_db,queryBody )
                return  new_reservation
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}")
async def Delete(id:int):        
        response = Facture_Service.Delete(id ,get_db )
        return  response