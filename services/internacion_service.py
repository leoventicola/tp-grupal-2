from schemas import InternacionCreate, InternacionUpdate
from pathlib import Path
from repositories.json_repositories import JsonRepository

repoMedico = JsonRepository(Path(__file__).parent.parent / "data" / "medicos.json")
repoPaciente = JsonRepository(Path(__file__).parent.parent / "data" / "pacientes.json")
repoInternacion = JsonRepository(Path(__file__).parent.parent / "data" / "internaciones.json")

def index():
    internaciones = repoInternacion.get_all()
    return [i for i in internaciones if not i["eliminado"]]

def create(internacion : InternacionCreate):

    medicos = repoMedico.get_all()
    pacientes = repoPaciente.get_all()
    internaciones = repoInternacion.get_all()

    siguiente_id = repoInternacion.next_id(internaciones)
    nuevo = internacion.model_dump()

    ok, msg = validPaciente(nuevo["paciente_id"])
    if not ok:
        return None, msg
    
    ok, msg = validMedico(nuevo["medico_id"])
    if not ok:
        return None, msg
    
    ok, msg = validNuevaInternacion(nuevo["paciente_id"])
    if not ok:
        return None, msg

    nuevo["id"] = siguiente_id
    nuevo["eliminado"] = False
    internaciones.append(nuevo)
    repoInternacion.save(internaciones)

    return nuevo, ""

def update(id : int ,internacion : InternacionUpdate):
    internaciones = repoInternacion.get_all()
    for item in internaciones:
        if item["id"] == id and not item["eliminado"]:
            datos = internacion.model_dump(exclude_unset = True)
            ok, msg = validMedico(datos["medico_id"])
            if not ok:
                return None, msg
            item.update(datos)
            repoInternacion.save(internaciones)
            return item, ""
    return None, "Internacion no encontrada"

def delete(id : int):
    internaciones = repoInternacion.get_all()
    for item in internaciones:
        if item["id"] == id and not item["eliminado"]:
            item["eliminado"] = True
            repoInternacion.save(internaciones)
            return True
    return False 

def validPaciente(id):
    pacientes = repoPaciente.get_all()
    for item in pacientes:
        if item["id"] == id and not item["eliminado"]:
            return True, ""
    return False, "Paciente no encontrado o eliminado"

def validMedico(id):
    medicos = repoMedico.get_all()
    for item in medicos:
        if item["id"] == id and not item["eliminado"]:
            return True, ""
    return False, "Medico no encontrado o eliminado"

def validNuevaInternacion(paciente_id):
    internaciones = repoInternacion.get_all()
    for item in internaciones:
        if item["paciente_id"] == paciente_id and not item["eliminado"]:
            return False, "El paciente ya se encuentra internado"
    return True, ""

    
