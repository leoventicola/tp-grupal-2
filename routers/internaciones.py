from fastapi import APIRouter, Depends,  HTTPException

from schemas import (
    InternacionCreate,
    InternacionUpdate,
    InternacionResponse
)

from services import internacion_service

router = APIRouter(prefix="/internaciones")

@router.get("/", response_model = list[InternacionResponse])
def index():
    return internacion_service.index()


@router.post("/", response_model = InternacionResponse)
def create(internacion : InternacionCreate):
    nueva_internacion =  internacion_service.create(internacion)
    if not nueva_internacion:
        raise HTTPException(status_code = 404, detail="Error: Valide que exista el medico y el paciente. Y el paciente no debe estar internado.")
    return nueva_internacion    

@router.patch("/{id}", response_model = InternacionResponse)
def update(id : int, internacion : InternacionUpdate):
    return internacion_service.update(id, internacion)

@router.delete("/{id}",status_code=204)
def delete(id : int):
    eliminado = internacion_service.delete(id)
    if not eliminado:
        raise HTTPException(status_code = 404, detail="Internacion no encontrada")
