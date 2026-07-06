from fastapi import APIRouter, Depends, HTTPException

from schemas import(
    MedicoCreate,
    MedicoUpdate,
    MedicoResponse
)

from services import medico_service

router = APIRouter(prefix="/medicos")

@router.get("/", response_model = list[MedicoResponse])
def index():
    return medico_service.index()

@router.post("/",response_model = MedicoResponse)
def create(medico : MedicoCreate):
    return medico_service.create(medico)

@router.get("/{id}", response_model = MedicoResponse)
def get(id : int):
    medico = medico_service.get(id)
    if not medico:
        raise HTTPException(status_code = 404, detail="Medico no encontrado")
    return medico    
