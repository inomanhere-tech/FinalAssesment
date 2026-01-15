from store import memory
from models.job import Job, JobCreate


def get_all_jobs():
    return memory.jobs


def get_job_by_id(job_id: int):
    for job in memory.jobs:
        if job.id == job_id:
            return job
    return None


def create_job(job: JobCreate):
    new_id = len(memory.jobs) + 1
    new_job = Job(id=new_id, **job.dict())
    memory.jobs.append(new_job)
    return new_job
