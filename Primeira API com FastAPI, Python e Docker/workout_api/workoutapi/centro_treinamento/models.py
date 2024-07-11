from sqlalchemy import Integer, String 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workoutapi.contrib.models import BaseModel, AtletaModel 


class CategoriaTreinamento(BaseModel):
    __tablename__= 'centros_treinamento'
    
    pk_id:Mapped[int] = mapped_column(Integer, primary_key=True)
    nome:Mapped[int] = mapped_column(String(50), unique=True, nullable=False)
    endereco:Mapped[int] = mapped_column(String(60), nullable=False)
    proprietario:Mapped[int] = mapped_column(String(30), nullable=False)
    atleta:Mapped['AtletaModel']= relationship(back_populates='centros_treinamento')
   