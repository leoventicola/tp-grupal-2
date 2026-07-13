from datetime import datetime
from pydantic import BaseModel

class PacienteBase(BaseModel):
    dni           : str
    nombre        : str
    apellido      : str
    edad          : int
    telefono      : str
    obra_social   : str

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(BaseModel):
    dni           : str | None = None
    nombre        : str | None = None
    apellido      : str | None = None
    edad          : int | None = None
    telefono      : str | None = None
    obra_social   : str | None = None

class PacienteResponse(PacienteBase):
    id            : int

class MedicoBase(BaseModel):
    matricula     : str
    nombre        : str
    apellido      : str
    especialidad  : str
    telefono      : str

class MedicoCreate(MedicoBase):
    pass

class MedicoUpdate(BaseModel):
    matricula     : str | None = None
    nombre        : str | None = None
    apellido      : str | None = None
    especialidad  : str | None = None
    telefono      : str | None = None

class MedicoResponse(MedicoBase):
    id            : int
    eliminado     : bool

class InternacionBase(BaseModel):
    paciente_id   : int
    medico_id     : int
    fecha_ingreso : str
    diagnostico   : str
    habitacion    : str
    estado        : str

class InternacionCreate(InternacionBase):
    pass

class InternacionUpdate(BaseModel):
    medico_id     : int | None = None
    fecha_ingreso : str | None = None
    diagnostico   : str | None = None
    habitacion    : str | None = None
    estado        : str | None = None

class InternacionResponse(InternacionBase):
    id           : int
    eliminado    : bool