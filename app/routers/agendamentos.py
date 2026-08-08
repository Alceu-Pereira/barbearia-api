from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import AgendamentoCreate, AgendamentoResponse
from app.services import agendamento_service

from datetime import datetime, date

router = APIRouter(prefix="/api/v1/agendamentos", tags=["Agendamentos"])

@router.post(
    "",
    response_model=AgendamentoResponse,
    status_code=status.HTTP_201_CREATED,
)
def criar(dados: AgendamentoCreate, db: Session = Depends(get_db)):
    try:
        return agendamento_service.criar_agendamento(
            db=db,
            cliente_id=dados.cliente_id,
            barbeiro_id=dados.barbeiro_id,
            servico_id=dados.servico_id,
            inicio=dados.data_hora_inicio,
        )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

@router.get("/disponibilidade", response_model=list[datetime])
def listar_disponibilidade(
    barbeiro_id: int,
    dia: date,
    servico_id: int,
    db: Session = Depends(get_db)
):
    try:
        return agendamento_service.horarios_disponiveis(
            db=db,
            barbeiro_id=barbeiro_id,
            dia=dia,
            servico_id=servico_id
        )
    except ValueError as erro:
        raise HTTPException(status_code=404, detail=str(erro))