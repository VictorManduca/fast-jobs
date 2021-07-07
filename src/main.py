from fastapi import FastAPI

from src.core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

@app.get("/")
def index():
  return 'pego véi'
