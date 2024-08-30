from fastapi import APIRouter, Body, HTTPException
from fastapi import APIRouter, Body, HTTPException
from config.db import get_db
from Service import FacturaProductsService as FacturaProducts_Service
from Schemas.Schemas import Factura_Product , Factura_Product_Post
router = APIRouter()
@router.get("/")
async def Get():
    try: 
        Reservations =  FacturaProducts_Service.Get(get_db) 
        return Reservations
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        

@router.get("/{id}")
async def Get_By_Id(id:int):
        try:       
                reservaton_Byid = FacturaProducts_Service.Get_By_Id(get_db,id )
                return  reservaton_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))       

@router.post("/")
async def Post(
        queryBody: Factura_Product_Post = Body(...)
        ):
        try:
                reservaton_Byid = FacturaProducts_Service.Post(get_db,queryBody )
                return  reservaton_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
        
@router.put("/")
async def Put(
        queryBody: Factura_Product = Body(...)
        ):
        try:       
                new_reservation = FacturaProducts_Service.Put(get_db,queryBody )
                return  new_reservation
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}")
async def Delete(id:int):        
        response = FacturaProducts_Service.Delete(id ,get_db )
        return  response