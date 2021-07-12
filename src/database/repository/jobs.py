from sqlalchemy.orm import Session

from src.schemas.jobs import JobCreate
from src.database.models.jobs import Jobs


def create_job(job: JobCreate, database: Session, owner_id: int):
    job = Jobs(**job.dict(), owner_id=owner_id)
    database.add(job)
    database.commit()
    database.refresh(job)

    return job
