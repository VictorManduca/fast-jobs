import random
import string

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.database.repository.users import create_user
from src.database.repository.users import get_user
from src.schemas.users import UserCreate


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def create_random_owner(database: Session):
    email = f"{random_lower_string()}@{random_lower_string()}.com"
    password = random_lower_string()
    user_schema = UserCreate(username=email, email=email, password=password)
    user = create_user(user=user_schema, database=database)
    return user


def user_authentication_headers(client: TestClient, email: str, password: str):
    data = {"username": email, "password": password}
    client_response = client.post("/login", data=data)
    response = client_response.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def authentication_token_from_email(client: TestClient, email: str, database: Session):
    """
    Return a valid token for the user with given email.
    If the user doesn't exist it is created first.
    """
    password = "random-passW0rd"
    user = get_user(username=email, database=database)
    if not user:
        user_in_create = UserCreate(username=email, email=email, password=password)
        user = create_user(user=user_in_create, database=database)
    return user_authentication_headers(client=client, email=email, password=password)
