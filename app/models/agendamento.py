from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from app.database import Base

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    barbeiro_id = Column(Integer, ForeignKey("barbeiros.id"), nullable=False)
    servico_id = Column(Integer, ForeignKey("servicos.id"), nullable=False)
    data_hora_inicio = Column(DateTime, nullable=False, index=True)
    data_hora_fim = Column(DateTime, nullable=False)
    preco_cobrado = Column(Numeric(10, 2), nullable=False)
    status = Column(String(20), nullable=False, default="AGENDANDO", index=True)
    