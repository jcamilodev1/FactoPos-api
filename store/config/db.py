from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:admin123@localhost:5433/mydatabase"
# DATABASE_URL = "postgresql+psycopg2://factouser:admin123@db:54322/mydatabase"

# Elimina `connect_args`
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
meta = MetaData()

get_db = engine.connect()
