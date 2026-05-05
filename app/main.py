from fastapi import FastAPI #Iniciar o FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# para rodar o codigo, executart no terrminal: uvicorn main:app --reload
#---------------------------------------------

from app.routers.reports import reports_router
from app.routers.transactions import transactions_router
from app.routers.user import user_router

app.include_router(reports_router)
app.include_router(transactions_router)
app.include_router(user_router)