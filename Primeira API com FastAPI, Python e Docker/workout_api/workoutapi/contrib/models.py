from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_colum





class BaseModel(DeclarativeBase):
    id: Mapped(UUID) = mapped_colum(PG_UUID(as_uuid=True)) 
    