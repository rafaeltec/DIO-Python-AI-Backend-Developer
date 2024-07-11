from datetime import datetime
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workoutapi.categorias.models import CategoriaModel, CentroTreinamentoModel
from workoutapi.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__='atletas'
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[int] = mapped_column(String(50), nullable=False)
    cpf:Mapped[int] = mapped_column(String(11),unique=True, nullable=False)
    idade:Mapped[int] = mapped_column(Integer, nullable=False)
    peso:Mapped[int] = mapped_column(float, nullable=False)
    altura:Mapped[int] = mapped_column(Integer, nullable=False)
    sexo:Mapped[int] = mapped_column(String(1), nullable=False) 
    created_at: Mapped[datetime] = mapped_column(datetime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id = Mapped[int] = mapped_column(ForeignKey('categorias.pk_id')) 
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta')
    centro_treinamento_id = Mapped[int] = mapped_column(ForeignKey('centros_treinamentos.pk_id')) 
    