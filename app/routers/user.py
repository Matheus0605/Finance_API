from fastapi import APIRouter

user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.get("/")
async def create_user():
    return {"mensagem": "Rota de criacao de usuario criada"}