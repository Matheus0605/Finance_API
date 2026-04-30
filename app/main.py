#Iniciar o FastAPI
from fastapi import FastAPI

app = FastAPI()
# para rodar o codigo, executart no terrminal: uvicorn main:app --reload
#---------------------------------------------

from app.routers.reports import reports_router
from app.routers.transactions import transactions_router
from app.routers.user import user_router

app.include_router(reports_router)
app.include_router(transactions_router)
app.include_router(user_router)