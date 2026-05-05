from app.models import db
from sqlalchemy.orm import sessionmaker


def pegar_sessao():
    try:
        Session = sessionmaker(bind=db) #Cria a conexao com o banco de dados
        session = Session() # Istancia essa conexao e abre a sessao
        yield session #retorna o valor da funcao sem finalizar ela, podendo fechar a sessao depois do que precisa ser feito no banco de dados
       
    finally: #Independente de dar erro em alguma linha do codigo o finally sera executado e a sessao sera fechada
        session.close()