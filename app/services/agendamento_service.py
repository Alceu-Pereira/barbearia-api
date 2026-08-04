from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models import Agendamento, Barbeiro, Cliente, Servico
from app.models.enums import StatusAgendamento

def existe_conflito(
        db: Session,
        barbeiro_id: int,
        inicio: datetime,
        fim: datetime,
) -> bool:

    conflito = (
        db.query(Agendamento).filter(
            Agendamento.barbeiro_id == barbeiro_id,
            Agendamento.status == StatusAgendamento.AGENDADO,
            Agendamento.data_hora_inicio < fim,
            Agendamento.data_hora_fim > inicio,
        ).first()
    )

    return conflito is not None

def criar_agendamento(
        db: Session,
        cliente_id: int,
        barbeiro_id: int,
        servico_id: int,
        inicio: datetime,
) -> Agendamento:
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente is None or not cliente.ativo:
        raise ValueError("Cliente nao encontrado ou inativo")