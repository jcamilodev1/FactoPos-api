from fastapi import FastAPI
from Controller import ClientController, FacturaController, ProductController



app = FastAPI()

app.include_router(ClientController.router, prefix="/Client", tags=["Client"])
app.include_router(FacturaController.router, prefix="/Facture", tags=["Facture"])
# app.include_router(ProductController.router, prefix="/Product", tags=["Product"])