from typing import Annotated
from pydantic import Field, PositiveFloat

from workoutapi.contrib.schemas import BaseModel, BaseSchema

class CentroTreinamento(BaseSchema):
   
    nome: Annotated[str, Field(description='Nome do centro de treinamento', examples='CT King', max_length=20)]
    endereco : Annotated[str, Field(description='Endereço do centro do treinamento', examples='Rua do tatuape 154', max_length=60)]
    Proprietario : Annotated[str, Field(description='Proprietário do centro de treinamento', examples='Rogério', max_length=30)]