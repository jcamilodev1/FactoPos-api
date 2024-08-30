from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from Controller import clientcontroller, FacturaController, ProductController, FacturaProductsController



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las origines, cambia esto según tus necesidades
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos, ajusta según sea necesario
    allow_headers=["*"],  # Permitir todos los encabezados, ajusta según sea necesario
)

app.include_router(clientcontroller.router, prefix="/Client", tags=["Client"])
app.include_router(FacturaController.router, prefix="/Factura", tags=["Factura"])
app.include_router(ProductController.router, prefix="/Product", tags=["Product"])
app.include_router(FacturaProductsController.router, prefix="/FacturaProduct", tags=["FacturaProduct"])