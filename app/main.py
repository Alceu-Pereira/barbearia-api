from fastapi import FastAPI

app = FastAPI(title="Barbearia API")

@app.get("/")
def ler_raiz():
    return {"mensagem": "A barbearia está aberta!"}

