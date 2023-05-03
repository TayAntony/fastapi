from fastapi import FastAPI, HTTPException, status, Response, Header, Query, Depends
from typing import Optional, Any, Dict
from models import Curso
from time import sleep


app = FastAPI()

cursos = {
    1:{
        "id": 1,
        "nome": "Curso de Python",
        "aulas": 20,
        "horas": 80,
        "instrutor": "Cleber"
    },
    2:{
        "id": 2,
        "nome": "Curso de Java",
        "aulas": 15,
        "horas": 60,
        "instrutor": "Leonardo"
    },
    3:{
        "id": 3,
        "nome": "Curso de Banco de Dados",
        "aulas": 12,
        "horas": 48,
        "instrutor": "Francis"
    },
}

def fake_db():
    try:
        print("Abrindo conexão com o banco")
        sleep(1)
    finally:
        print('Fechando conexão com o banco')
        sleep(1)


@app.get("/cursos", description="Retorna todos os cursos ou uma lista vazia!", summary="Retorna tudo!", response_model=Dict[int, Curso])
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos



@app.get("/cursos/{curso_id}")
async def get_cursos(curso_id:int):
    try:
        curso = cursos[curso_id]
        #curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')



@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    if curso.id not in cursos:
        next_id = len(cursos) + 1
        curso.id = next_id
        #curso.update({"id": next_id})
        cursos[next_id]= curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Já existe um curso com o ID {curso.id}')



@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    for key, value in cursos.items():
        pass
    next_id = key + 1
    if curso_id in cursos:
        cursos[next_id] = curso
        cursos[next_id].id = next_id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Já existe um curso com o id {curso.id}')



@app.delete("/cursos/deletar/{curso_id}")
async def deletar_cursos(curso_id:int):
    if curso_id in cursos:
        del cursos[curso_id]
        return HTTPException(status_code=204, detail="Esse curso foi apagado com sucesso")
    else:
        return HTTPException(status_code=404, detail="Esse curso não foi encontrado")



@app.get("/calculadora")
async def calcular(a: int = Query(default=None, gt=5), b:int=Query(default=None, gt=10), user: str = Header(default=None), c : Optional[int] = 0):
    soma = a+b+c
    print(f'usuario: {user}')
    return (f'Resultdo: {soma}')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host = '127.0.0.1', port = 8000, log_level="info", reload=True)