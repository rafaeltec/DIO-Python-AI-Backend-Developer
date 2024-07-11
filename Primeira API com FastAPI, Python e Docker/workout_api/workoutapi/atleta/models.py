from datetime import datetime
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from workoutapi.contrib.models import BaseModel


class AtletaMode(BaseModel):
    __tablename__='atletas'
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[int] = mapped_column(String(50), nullable=False)
    cpf:Mapped[int] = mapped_column(String(11), nullable=False)
    idade:Mapped[int] = mapped_column(Integer, nullable=False)
    peso:Mapped[int] = mapped_column(float, nullable=False)
    altura:Mapped[int] = mapped_column(Integer, nullable=False)
    sexo:Mapped[int] = mapped_column(String(1), nullable=False) 
    created_at: Mapped[datetime] = mapped_column(datetime, nullable=False)