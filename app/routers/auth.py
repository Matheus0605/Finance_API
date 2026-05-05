from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Usuario
from app.dependencies import pegar_sessao
from app.main import bcrypt_context
from app.schemas import LoginSchema


auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter(Usuario.email == login_schema.email).first()

    if not usuario:
        raise HTTPException(status_code=400, detail="Email ou senha inválidos")

    if not bcrypt_context.verify(login_schema.password, usuario.password):
        raise HTTPException(status_code=400, detail="Email ou senha inválidos")

    return {"mensagem": "Login realizado com sucesso"}