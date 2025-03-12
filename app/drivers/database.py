import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

Base = declarative_base()

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("SUPABASE_USER"),
    password=os.getenv("SUPABASE_PASSWORD"),
    host=os.getenv("SUPABASE_HOST"),
    port=int(os.getenv("SUPABASE_PORT")),
    database=os.getenv("SUPABASE_DB_NAME")
)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
