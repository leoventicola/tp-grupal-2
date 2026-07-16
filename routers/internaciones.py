from fastapi import APIRouter, Depends,  HTTPException

from schemas import (
    InternacionCreate,
    InternacionUpdate,
    InternacionResponse
)

from services import internacion_service
from auth import verify_token

router = APIRouter(
    prefix="/internaciones",
    dependencies=[Depends(verify_token)]
)

@router.get("/", response_model = list[InternacionResponse])
def index():
    return internacion_service.index()


@router.post("/", response_model = InternacionResponse)
def create(internacion : InternacionCreate):
    resultado, mensaje = internacion_service.create(internacion)
    if not resultado:
        raise HTTPException(status_code = 400, detail=mensaje)
    return resultado    

@router.put("/{id}", response_model = InternacionResponse)
def update(id : int, internacion : InternacionUpdate):
    resultado, mensaje = internacion_service.update(id, internacion)
    if not resultado:
        raise HTTPException(status_code = 404, detail=mensaje)
    return resultado

@router.delete("/{id}",status_code=204)
def delete(id : int):
    eliminado = internacion_service.delete(id)
    if not eliminado:
        raise HTTPException(status_code = 404, detail="Internacion no encontrada")

@router.get("/{id}", response_model=InternacionResponse)
def get(id: int):
    internacion = internacion_service.get(id)

    if not internacion:
        raise HTTPException(
            status_code=404,
            detail="Internacion no encontrada"
        )

    return internacion