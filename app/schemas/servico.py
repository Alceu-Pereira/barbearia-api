from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

class ServicoBase(BaseModel):
    nome: str = Field(min_length=2, max_length=100)
    duracao_minutos: int = Field(gt=0, le=480)
    preco: Decimal = Field(gt=0, decimal_places=2)

class ServicoCreate(ServicoBase):
    pass

class ServicoResponse(ServicoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)