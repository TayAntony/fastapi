from typing import Opitional
from pydantic import BaseMoel as SchemaBaseModel
class CursoSchema(SchemaBaseModel):
    id: Opitional[int]
    titulo: str
    aulas: int
    horas: int
    instrutor: str

    class Config:
        orm_mode = True