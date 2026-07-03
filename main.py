from fastapi import FastAPI

from routers import pacientes

app = FastAPI()

app.include_router(pacientes.router)