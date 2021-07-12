from sqlalchemy.orm import Session

from src.schemas.jobs import JobCreate, JobUpdate
from src.database.models.jobs import Jobs


def create_job(job: JobCreate, database: Session, owner_id: int):
    job = Jobs(**job.dict(), owner_id=owner_id)
    database.add(job)
    database.commit()
    database.refresh(job)

    return job


def retrieve_job(job_id: int, database: Session):
    job = database.query(Jobs).filter(Jobs.id == job_id).first()
    return job


def retrieve_all_jobs(database: Session):
    jobs = database.query(Jobs).all()
    return jobs


def retrieve_all_active_jobs(database: Session):
    jobs = database.query(Jobs).filter(Jobs.is_active).all()
    return jobs


def update_job_by_id(job_id: int, job: JobUpdate, database: Session, owner_id: int):
    is_exist_job = database.query(Jobs).filter(Jobs.id == job_id)
    if not is_exist_job.first():
        return False
    else:
        job = job.dict(exclude_unset=True)
        job.update(owner_id=owner_id)
        is_exist_job.update(job)
        database.commit()
        return True


def delete_job_by_id(job_id: int, database: Session):
    is_exist_job = database.query(Jobs).filter(Jobs.id == job_id)
    if not is_exist_job.first():
        return False
    else:
        is_exist_job.delete(synchronize_session=False)
        database.commit()
        return True
