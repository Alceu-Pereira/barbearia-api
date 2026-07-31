from sqlalchemy import Column, Integer, String, Numeric
from app.database import Base

class Servico(Base):
    __tablename__ = "servicos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    duracao_minutos = Column(Integer, nullable=False)
    preco = Column(Numeric(10, 2), nullable=False)