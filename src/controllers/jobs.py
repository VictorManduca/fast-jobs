from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.session import get_db
from src.database.repository.jobs import create_job
from src.schemas.jobs import JobCreate, ShowJob

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ShowJob)
def route_create_job(job: JobCreate, database: Session = Depends(get_db)):
    try:
        owner_id = 1
        job = create_job(job=job, database=database, owner_id=owner_id)
        return job
    except BaseException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong. Error: {}".format(exception)
        )
