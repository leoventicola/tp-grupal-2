from pydantic import BaseModel, Field


class PacienteBase(BaseModel):
    dni           : str
    nombre        : str
    apellido      : str
    edad          : int = Field(gt=0)
    telefono      : str
    obra_social   : str

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(BaseModel):
    dni           : str | None = None
    nombre        : str | None = None
    apellido      : str | None = None
    edad          : int | None = Field(default=None, gt=0)
    telefono      : str | None = None
    obra_social   : str | None = None

class PacienteResponse(PacienteBase):
    id            : int

class MedicoBase(BaseModel):
    matricula     : str = Field(min_length=1)
    nombre        : str = Field(min_length=1)
    apellido      : str = Field(min_length=1)
    especialidad  : str = Field(min_length=1)
    telefono      : str

class MedicoCreate(MedicoBase):
    pass

class MedicoUpdate(BaseModel):
    matricula     : str | None = Field(default=None, min_length=1)
    nombre        : str | None = Field(default=None, min_length=1)
    apellido      : str | None = Field(default=None, min_length=1)
    especialidad  : str | None = Field(default=None, min_length=1)
    telefono      : str | None = None

class MedicoResponse(MedicoBase):
    id            : int
    eliminado     : bool

class InternacionBase(BaseModel):
    paciente_id   : int
    medico_id     : int
    fecha_ingreso : str = Field(min_length=1)
    diagnostico   : str = Field(min_length=1)
    habitacion    : int = Field(gt=0)
    estado        : str = Field(min_length=1)

class InternacionCreate(InternacionBase):
    pass

class InternacionUpdate(BaseModel):
    medico_id     : int | None = None
    fecha_ingreso : str | None = Field(default=None, min_length=1)
    diagnostico   : str | None = Field(default=None, min_length=1)
    habitacion    : int | None = Field(default=None, gt=0)
    estado        : str | None = Field(default=None, min_length=1)

class InternacionResponse(InternacionBase):
    id           : int
    eliminado    : bool