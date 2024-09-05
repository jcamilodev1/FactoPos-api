from fastapi import APIRouter, Body, HTTPException
from fastapi import APIRouter, Body, HTTPException
from config.db import get_db
from Service.ProductService import ProductService

from Schemas.Schemas import Product , Product_Post
router = APIRouter()
@router.get("/")
async def Get():
    try: 
        Reservations =  ProductService.Get(get_db) 
        return Reservations
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        

@router.get("/{id}")
async def Get_By_Id(id:int):
        try:       
                reservaton_Byid = ProductService.Get_By_Id(get_db,id )
                return  reservaton_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))       

@router.post("/")
async def Post(
        queryBody: Product_Post = Body(...)
        ):
        try:
                reservaton_Byid = ProductService.Post(get_db,queryBody )
                return  reservaton_Byid
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
        
@router.put("/")
async def Put(
        queryBody: Product = Body(...)
        ):
        try:       
                new_reservation = ProductService.Put(get_db,queryBody )
                return  new_reservation
        except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}")
async def Delete(id:int):        
        response = ProductService.Delete(id ,get_db )
        return  response