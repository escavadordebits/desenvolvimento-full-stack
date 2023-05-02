from pydantic import BaseModel
from typing import Optional, List
from model.carro import Carro

from schemas import ComentarioSchema


class CarroSchema(BaseModel):
    """ Define como um novo Carro a ser inserido deve ser representado
    """
    nome: str = "Opala"
    quantidade: Optional[int] = 12
    valor: float = 12.50


class CarroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do Carro.
    """
    nome: str = "Teste"


class ListagemCarrosSchema(BaseModel):
    """ Define como uma listagem de Carros será retornada.
    """
    Carros: List[CarroSchema]


def apresenta_Carros(Carros: List[Carro]):
    """ Retorna uma representação do Carro seguindo o schema definido em
        CarroViewSchema.
    """
    result = []
    for Carro in Carros:
        result.append({
            "nome": Carro.nome,
            "quantidade": Carro.quantidade,
            "valor": Carro.valor,
        })

    return {"Carros": result}


class CarroViewSchema(BaseModel):
    """ Define como um Carro será retornado: Carro + comentários.
    """
    id: int = 1
    nome: str = "Banana Prata"
    quantidade: Optional[int] = 12
    valor: float = 12.50
    total_cometarios: int = 1
    comentarios: List[ComentarioSchema]


class CarroDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str


def apresenta_Carro(Carro: Carro):
    """ Retorna uma representação do Carro seguindo o schema definido em
        CarroViewSchema.
    """
    return {
        "id": Carro.id,
        "nome": Carro.nome,
        "quantidade": Carro.quantidade,
        "valor": Carro.valor,
        "total_cometarios": len(Carro.comentarios),
        "comentarios": [{"texto": c.texto} for c in Carro.comentarios]
    }
