from schemas import MedicoCreate, MedicoUpdate
from pathlib import Path
from repositories.json_repositories import JsonRepository

repo = JsonRepository(Path(__file__).parent.parent / "data" / "medicos.json")

def index():
    medicos = repo.get_all()
    return [m for m in medicos if not m["eliminado"]]

def create(medico : MedicoCreate):
    medicos = repo.get_all()
    siguiente_id = repo.next_id(medicos)
    nuevo = medico.model_dump()
    nuevo["id"] = siguiente_id
    nuevo["eliminado"] = False
    medicos.append(nuevo)
    repo.save(medicos)
    return nuevo

def get(id : int):
    medicos = repo.get_all()
    for item in medicos:
        if item["id"] == id and not item["eliminado"]:
            return item
    return None

def update(id : int, medico : MedicoUpdate):
    medicos = repo.get_all()
    for item in medicos:
        if item["id"] == id and not item["eliminado"]:
            datos = medico.model_dump(exclude_unset = True)
            item.update(datos)
            repo.save(medicos)
            return item
    return None

def delete(id : int):
    medicos = repo.get_all()
    for item in medicos:
        if item["id"] == id and not item["eliminado"]:
            item["eliminado"] = True
            repo.save(medicos)
            return True
    return False
    
def update(id: int, medico: MedicoUpdate):
    medicos = repo.get_all()

    for item in medicos:
        if item["id"] == id and not item["eliminado"]:

            datos = medico.model_dump(exclude_none=True)

            for campo, valor in datos.items():
                item[campo] = valor

            repo.save(medicos)
            return item

    return None