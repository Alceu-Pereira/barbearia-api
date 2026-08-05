from fastapi import FastAPI
from app.routers import health, agendamentos
from app.database import criar_tabelas
from app.models import cliente, barbeiro, servico, agendamento

app = FastAPI(title="Barbearia API")
criar_tabelas()

app.include_router(health.router)
app.include_router(agendamentos.router)
