from schemas import PacienteCreate, PacienteUpdate
from pathlib import Path
from repositories.json_repositories import JsonRepository

repo = JsonRepository(Path(__file__).parent.parent / "data" / "pacientes.json")

def index():
    pacientes = repo.get_all()
    return [p for p in pacientes if not p["eliminado"]]

def create(paciente : PacienteCreate):
    nuevo = paciente.model_dump()
    return nuevo

def update(id : int, paciente : PacienteUpdate):
    nuevo = paciente
    nuevo[id] = 1
    nuevo["eliminado"] = False
    return nuevo