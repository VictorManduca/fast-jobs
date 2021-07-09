from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator, final

from src.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
  try:
    db = SessionLocal()
    yield
  finally:
    db.close()