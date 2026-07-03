from schemas import PacienteCreate, PacienteUpdate
from pathlib import Path
from repositories.json_repositories import JsonRepository

repo = JsonRepository(Path(__file__).parent.parent / "data" / "pacientes.json")

def index():
    pacientes = repo.get_all()
    return [p for p in pacientes if not p["eliminado"]]

def create(paciente : PacienteCreate):
    pacientes = repo.get_all()
    siguiente_id = repo.next_id(pacientes)
    nuevo = paciente.model_dump()
    nuevo["id"] = siguiente_id
    nuevo["eliminado"] = False
    pacientes.append(nuevo)
    repo.save(pacientes)
    return nuevo

def get(id : int):
    pacientes = repo.get_all()
    for item in pacientes:
        if item["id"] == id and not item["eliminado"]:
            return item
    return None

def update(id : int, paciente : PacienteUpdate):
    pacientes = repo.get_all()
    for item in pacientes:
        if item["id"] == id and not item["eliminado"]:
            datos = paciente.model_dump(exclude_unset = True)
            item.update(datos)
            repo.save(pacientes)
            return item
    return None

def delete(id : int):
    pacientes = repo.get_all()
    for item in pacientes:
        if item["id"] == id and not item["eliminado"]:
            item["eliminado"] = True
            repo.save(pacientes)
            return True
    return False
