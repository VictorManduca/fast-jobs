from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.controllers.auth import get_current_user_from_token
from src.schemas.users import UserCreate, ShowUser
from src.database.class_models import Users
from src.database.session import get_db
from src.database.repository.users import create_user

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def route_create_user(user: UserCreate, database: Session = Depends(get_db),
                      current_user: Users = Depends(get_current_user_from_token)):
    try:
        user = create_user(user, database)
        return user
    except IntegrityError as exception:
        raise exception("Duplicated key")
    except BaseException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong. Error: {}".format(exception)
        )
