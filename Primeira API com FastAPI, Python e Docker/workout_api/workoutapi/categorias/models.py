from sqlalchemy import Integer, String 
from sqlalchemy.orm import Mapped, mapped_column
from workoutapi.contrib.models import BaseModel


class CategoriaModel(BaseModel):
    __tablename__='categorias'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[int] = mapped_column(String(50), nullable=False)
   