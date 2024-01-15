from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from fastapi_event import FastAPI

app = FastAPI()
database = []


class Events(BaseModel):
    nome: str
    dono: str
    descricao: str
    data: str
    quantidade_ingressos: int
    ingressos_vendidos: int
    data_validade: str


@app.get('/')
async def hello_world() -> str:
    return 'Hello World'


@app.post('/event', response_model=Events)
async def criar_evento(event: Events):
    database.append(event)

    return event


@app.get('/event')
async def ler_todos_os_eventos() -> List[Events]:
    return database
