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
    
    barbeiro = db.query(Barbeiro).filter(Barbeiro.id == barbeiro_id).first()
    if barbeiro is None or not barbeiro.ativo:
        raise ValueError("Barbeiro nao encontrado ou inativo")

    servico = db.query(Servico).filter(Servico.id == servico_id).first()
    if servico is None:
        raise ValueError("Servico nao encontrado")

    fim = inicio + timedelta(minutes=servico.duracao_minutos)

    if existe_conflito(db, barbeiro_id, inicio, fim):
        raise ValueError("Horario indisponivel para este barbeiro")

    agendamento = Agendamento(
        cliente_id=cliente_id,
        barbeiro_id=barbeiro_id,
        servico_id=servico_id,
        data_hora_inicio=inicio,
        data_hora_fim=fim,
        preco_cobrado=servico.preco,
        status=StatusAgendamento.AGENDADO,
    )

    db.add(agendamento)
    db.commit()
    db.refresh(agendamento)
    return agendamento