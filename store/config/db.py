from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///app/store/database.db"  # Cambia esta URL a la de tu base de datos

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
meta = MetaData()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
