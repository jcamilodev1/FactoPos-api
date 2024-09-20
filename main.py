from fastapi import FastAPI
from controllers import user_controller

app = FastAPI()

# Registrar el router para los endpoints de usuarios
app.include_router(user_controller.router)

# Endpoint de prueba
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
