from fastapi import FastAPI

from routers import pacientes, medicos, internaciones 

app = FastAPI()

app.include_router(pacientes.router)
app.include_router(medicos.router)
app.include_router(internaciones.router)