from fastapi import APIRouter

transactions_router = APIRouter(prefix="/transactions", tags=["transactions"])

@transactions_router.get("/")
async def trans():
    return {"mensagem": "Criado a rota de transacoes"}