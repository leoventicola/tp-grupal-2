from fastapi import APIRouter, Depends

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