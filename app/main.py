from fastapi import FastAPI
from app.routers import health
from app.database import criar_tabelas
from app.models import cliente, barbeiro

app = FastAPI(title="Barbearia API")
criar_tabelas()

app.include_router(health.router)
