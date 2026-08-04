from pydantic import BaseModel, ConfigDict, Field

class BarbeiroBase(BaseModel):
    nome: str = Field(min_length=2, max_length=100)

class BarbeiroCreate(BarbeiroBase):
    pass

class BarbeiroResponse(BarbeiroBase):
    id: int
    ativo: bool
    
    model_config = ConfigDict(from_attributes=True)