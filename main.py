from fastapi import FastAPI, Depends

from routers import pacientes, medicos, internaciones 
from auth import verify_token

app = FastAPI(dependencies=[Depends(verify_token)])

app.include_router(pacientes.router)
app.include_router(medicos.router)
app.include_router(internaciones.router)
