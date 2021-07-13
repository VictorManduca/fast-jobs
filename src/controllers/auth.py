from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from src.core.config import settings
from src.core.hash import Hasher
from src.core.security import create_access_token
from src.database.session import get_db
from src.database.repository.users import get_user

router = APIRouter()


def authenticate_user(username: str, password: str, database: Session):
    user = get_user(username=username, database=database)
    if not user:
        return False
    elif not Hasher.verify_password(password, user.hashed_password):
        return False
    else:
        return user


@router.post("/login", status_code=status.HTTP_200_OK)
def route_login(form_data: OAuth2PasswordRequestForm = Depends(), database: Session = Depends(get_db)):
    try:
        user = authenticate_user(form_data.username, form_data.password, database)
        if not user:
            raise Exception("Incorrect email or password")
        else:
            access_token_expire = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expire)

            return {
                "access_token": access_token,
                "token_type": "bearer"
            }
    except BaseException as exception:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Something went wrong. Error: {}".format(exception)
        )


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user_from_token(token: str = Depends(oauth2_scheme), database: Session = Depends(get_db)):
    try:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )

        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        print("sabosta eh: ", username)

        if username is None:
            raise credentials_exception

        user = get_user(username=username, database=database)
        if user is None:
            raise credentials_exception

        return user
    except JWTError:
        return credentials_exception
    except BaseException as exception:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Something went wrong. Error: {}".format(exception)
        )
