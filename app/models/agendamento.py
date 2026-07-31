from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey, Enum
from app.database import Base
from app.models.enums import StatusAgendamento

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    barbeiro_id = Column(Integer, ForeignKey("barbeiros.id"), nullable=False)
    servico_id = Column(Integer, ForeignKey("servicos.id"), nullable=False)
    data_hora_inicio = Column(DateTime, nullable=False, index=True)
    data_hora_fim = Column(DateTime, nullable=False)
    preco_cobrado = Column(Numeric(10, 2), nullable=False)
    status = Column(
        Enum(StatusAgendamento, create_constraint=True, validate_strings=True), nullable=False, 
        default=StatusAgendamento.AGENDADO, 
        index=True
        )
