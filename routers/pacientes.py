from fastapi import APIRouter, Depends,  HTTPException

from schemas import (
    PacienteCreate,
    PacienteUpdate,
    PacienteResponse
)

from services import paciente_service

router = APIRouter(prefix="/pacientes")

@router.get("/", response_model = list[PacienteResponse])
def index():
    return paciente_service.index()


@router.post("/", response_model = PacienteResponse)
def create(paciente : PacienteCreate):
    return paciente_service.create(paciente)

@router.patch("/{id}" ,response_model = PacienteResponse)
def update(id : int, paciente : PacienteUpdate):
    return paciente_service.update(id, paciente)

@router.get("/{id}", response_model = PacienteResponse)
def get(id : int):
    return paciente_service.get(id)

@router.delete("/{id}", status_code = 204)
def delete(id : int):
    eliminado = paciente_service.delete(id)
    if not eliminado:
        raise HTTPException(status_code = 404, detail="Paciente no encontrado")