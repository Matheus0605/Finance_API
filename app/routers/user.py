from fastapi import APIRouter, Depends, HTTPException
from app.models import Usuario
from app.dependencies import pegar_sessao
from app.main import bcrypt_context
from app.schemas import UsuarioSchema
from sqlalchemy.orm import Session

user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.get("/")
async def home():
    return {"mensagem": "Rota de criacao de usuario criada"}

@user_router.post("/create_user")
async def create_user(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()

    if usuario:
        raise HTTPException(status_code=400, detail="Email do usuario ja cadastrado")
    
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.password)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"usuario cadastrado com sucesso {usuario_schema.email}"}
