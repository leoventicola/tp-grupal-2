from pydantic import BaseModel, Field, field_validator


class PacienteBase(BaseModel):
    dni           : str
    nombre        : str 
    apellido      : str 
    edad          : int = Field(gt=0)
    telefono      : str
    obra_social   : str


    @field_validator("nombre","apellido")
    @classmethod
    def validar(cls,valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacio")
        return valor.strip()

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(PacienteBase):
    pass

class PacienteResponse(PacienteBase):
    id            : int

class MedicoBase(BaseModel):
    matricula     : str 
    nombre        : str
    apellido      : str 
    especialidad  : str 
    telefono      : str

    @field_validator("matricula","especialidad")
    @classmethod
    def validar(cls,valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacio")
        return valor.strip()

class MedicoCreate(MedicoBase):
    pass

class MedicoUpdate(BaseModel):
    pass

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