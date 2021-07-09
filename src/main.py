from fastapi import FastAPI

from src.core.config import settings
from src.database.session import engine
from src.database.class_models import Base

def create_tables():
  Base.metadata.create_all(bind=engine)

def start_up():
  app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
  create_tables()

  return app

app = start_up()

@app.get("/")
def index():
  return { 
    'status': 'ok'
  }