from fastapi import FastAPI
from app.routers import health

app = FastAPI(title="Barbearia API")

app.include_router(health.router)