from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

from src.schemas.users import UserCreate, ShowUser
from src.database.session import get_db
from src.database.repository.users import create_user

router = APIRouter()


@router.post("", status_code=201, response_model=ShowUser)
def route_create_user(user: UserCreate, database: Session = Depends(get_db)):
    try:
        user = create_user(user, database)
        return user
    except IntegrityError as exception:
        raise HTTPException(status_code=400, detail="Duplicated key")
    except BaseException as exception:
        raise HTTPException(status_code=400, detail="Something went wrong. Error: {}".format(exception))
