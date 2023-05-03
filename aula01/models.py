from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None #opcional para o usuário não precisar 'adivinhar' qual id será o proximo
    nome: str
    aulas: int
    horas: int
    instrutor: str

    @validator('nome')
    def validar_nome(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O nome precisa ter pelo menos 3 palavras...')
        return value