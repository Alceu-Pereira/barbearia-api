from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=False, index=True)
    ativo = Column(Boolean, default=True, nullable=False)