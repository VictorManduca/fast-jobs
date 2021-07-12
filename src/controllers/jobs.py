from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.session import get_db
from src.schemas.jobs import JobCreate, JobUpdate, ShowJob
from src.database.repository.jobs import (
    create_job,
    retrieve_job,
    retrieve_all_jobs,
    retrieve_all_active_jobs,
    update_job_by_id,
    delete_job_by_id
)

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


@router.get("/{job_id}", response_model=ShowJob)
def route_retrieve_job(job_id: int, database: Session = Depends(get_db)):
    try:
        job = retrieve_job(job_id=job_id, database=database)
        if not job:
            raise Exception("The given job id ({}) does not exist".format(job_id))
        else:
            return job
    except BaseException as exception:
        print("Ex: {}".format(exception))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong. Error: {}".format(exception)
        )


@router.get("")
def route_retrieve_jobs(database: Session = Depends(get_db)):
    try:
        jobs = retrieve_all_jobs(database=database)
        if not jobs:
            return []
        else:
            return jobs
    except BaseException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong. Error: {}".format(exception)
        )


@router.get("/all/active")
def route_retrieve_all_active_jobs(database: Session = Depends(get_db)):
    try:
        jobs = retrieve_all_active_jobs(database=database)
        if not jobs:
            return []
        else:
            return jobs
    except BaseException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong. Error: {}".format(exception)
        )


@router.patch("/{job_id}", status_code=status.HTTP_200_OK)
def route_update_job(job_id: int, job: JobUpdate, database: Session = Depends(get_db)):
    try:
        owner_id = 1
        is_successfully_updated = update_job_by_id(
            job_id=job_id,
            job=job,
            database=database,
            owner_id=owner_id
        )

        if not is_successfully_updated:
            raise Exception("The given job id does not exist")
    except BaseException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong. Error: {}".format(exception)
        )


@router.delete("/{job_id}", status_code=status.HTTP_200_OK)
def route_delete_job(job_id: int, database: Session = Depends(get_db)):
    try:
        owner_id = 1
        is_successfully_deleted = delete_job_by_id(job_id=job_id, database=database)

        if not is_successfully_deleted:
            raise Exception("The given job id does not exist")
    except BaseException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong. Error: {}".format(exception)
        )
