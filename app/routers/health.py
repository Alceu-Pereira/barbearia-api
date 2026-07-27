from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["Saúde"])

@router.get("/health")
def verificar_saude():
    return {"status": "ok", "mensagem": "A barbearia está aberta!"}