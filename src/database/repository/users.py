from sqlalchemy.orm import Session

from src.schemas.users import UserCreate
from src.database.models.users import Users
from src.core.hash import Hasher


def create_user(user:UserCreate, database:Session):
    user = Users(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False
    )

    database.add(user)
    database.commit()
    database.refresh(user)

    return user


def get_user(username: str, database: Session):
    user = database.query(Users).filter(Users.email == username).first()
    return user
