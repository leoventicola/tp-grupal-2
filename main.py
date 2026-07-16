from fastapi import FastAPI, Depends

from routers import pacientes, medicos, internaciones 
from auth import verify_token

app = FastAPI()

app.include_router(pacientes.router)
app.include_router(medicos.router)
app.include_router(internaciones.router)


