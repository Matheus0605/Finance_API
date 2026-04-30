from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

from datetime import datetime
from sqlalchemy import DateTime


# Cria conexao do banco
db = create_engine("sqlite:///banco.db")

# Cria a base do banco de dados
Base = declarative_base()

# Criar as classes/tabelas do banco
    # Usuario
class Usuario(Base):
    __tablename__="usuarios"


    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String, nullable=False)
    password_hash = Column("password_hash", String)

    def __init__(self, name, email, password_hash):

        self.name = name
        self.email = email
        self.password_hash = password_hash

class Transaction(Base):
    __tablename__="transactions"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_id = Column("usuario", Integer, ForeignKey("usuarios.id"))
    type = Column("type", String) # ENTRADA (inicome) OU SAIDA (expense) de dinheiro
    description = Column("description", String) #Especifica o que vai ser feito (exemplo: "Compra no mercado")
    value = Column("value", Float)
    category = Column("categoria", String)
    date = Column(DateTime, default=datetime.utcnow) # Dessa forma salva a data e hora atual 