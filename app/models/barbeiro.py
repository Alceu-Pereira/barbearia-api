from sqlalchemy import Column, String, Integer, Boolean
from app.database import Base

class Barbeiro(Base):
    __tablename__ = "barbeiros"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)
