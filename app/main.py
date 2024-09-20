from fastapi import FastAPI, HTTPException
from .schemas import UserLogin
from .auth import verify_password, get_user, create_access_token
from datetime import timedelta

# Define la cantidad de minutos que durará el token de acceso
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Puedes ajustar el valor según tus necesidades

app = FastAPI()

@app.post("/login")
def login(user: UserLogin):
    db_user = get_user(user.username)
    if db_user is None or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
