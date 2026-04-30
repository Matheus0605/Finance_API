from fastapi import APIRouter

reports_router = APIRouter(prefix="/reports", tags=["reports"])


@reports_router.get("/")
async def report():
    return {"mensagem": "Rota de report criada"}