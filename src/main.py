from fastapi import FastAPI

from src.core.config import settings
from src.database.session import engine
from src.database.class_models import Base

from src.routes import api_router

def create_tables():
    Base.metadata.create_all(bind=engine)

def include_routes(app: FastAPI):
    app.include_router(api_router)

def start_up():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    include_routes(app)

    return app

app = start_up()
