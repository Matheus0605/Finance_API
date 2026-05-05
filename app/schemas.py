from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    password: str

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True
    
