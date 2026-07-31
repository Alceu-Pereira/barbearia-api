from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}, # Só para SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def criar_tabelas():
    from app import models  # noqa: F401 - registra os modelos na Base
    Base.metadata.create_all(bind=engine)

@event.listens_for(engine, "connect")
def ativar_foreign_keys(conexao, _):
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
    