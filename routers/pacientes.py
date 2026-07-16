from fastapi import APIRouter, Depends,  HTTPException

from schemas import (
    PacienteCreate,
    PacienteUpdate,
    PacienteResponse
)

from services import paciente_service
from auth import verify_token

router = APIRouter(
    prefix="/pacientes",
    dependencies=[Depends(verify_token)]
)

@router.get("/", response_model = list[PacienteResponse])
def index():
    return paciente_service.index()


@router.post("/", response_model = PacienteResponse)
def create(paciente : PacienteCreate):
    return paciente_service.create(paciente)

@router.put("/{id}" ,response_model = PacienteResponse)
def update(id : int, paciente : PacienteUpdate):
    actualizado = paciente_service.update(id, paciente)
    if not actualizado:
        raise HTTPException(
            status_code = 404,
            detail="Paciente no encontrado")
    return actualizado

@router.get("/{id}", response_model = PacienteResponse)
def get(id : int):
    paciente = paciente_service.get(id)
    if not paciente:
        raise HTTPException(
            status_code = 404,
            detail="Paciente no encontrado")
    return paciente

@router.delete("/{id}", status_code = 204)
def delete(id : int):
    eliminado = paciente_service.delete(id)
    if not eliminado:
        raise HTTPException(status_code = 404, detail="Paciente no encontrado")