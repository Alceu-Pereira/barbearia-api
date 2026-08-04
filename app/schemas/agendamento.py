from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

from app.models.enums import StatusAgendamento



class AgendamentoCreate(BaseModel):
    cliente_id: int
    barbeiro_id: int
    servico_id: int
    data_hora_inicio: datetime

class AgendamentoResponse(BaseModel):
    id: int
    cliente_id: int
    servico_id: int
    data_hora_inicio: datetime
    data_hora_fim: datetime
    preco_cobrado: Decimal
    status: StatusAgendamento

    model_config = ConfigDict(from_attributes=True)