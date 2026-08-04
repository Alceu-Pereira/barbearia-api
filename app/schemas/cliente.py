from pydantic import BaseModel, Field, ConfigDict

class ClienteBase(BaseModel):
    nome: str = Field(min_length=2, max_length=100)
    telefone: str = Field(min_length=8, max_length=20)

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int
    ativo: bool

    model_config = ConfigDict(from_attributes=True)