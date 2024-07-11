from typing import Annotated
from workoutapi.contrib.schemas import BaseModel, BaseSchema
from pydantic import Field


class Categoria(BaseModel):
   
    nome: Annotated[str, Field(description='Nome da categoria', examples='Scale', max_length=10)]
    