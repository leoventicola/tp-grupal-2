from fastapi import FastAPI

from routers import pacientes, medicos

app = FastAPI()

app.include_router(pacientes.router)
app.include_router(medicos.router)