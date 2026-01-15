from fastapi import APIRouter, HTTPException
from typing import List
from models.job import Job, JobCreate
from store.memory import jobs_seed  # Use in-memory seed

router = APIRouter()


@router.get("/", response_model=list[Job])
def get_jobs():
    return jobs_seed


@router.get("/{job_id}", response_model=Job)
def get_job(job_id: int):
    for job in jobs_seed:
        if job["id"] == job_id:
            return job
    raise HTTPException(status_code=404, detail="Job not found")


@router.post("/", response_model=Job)
def create_job(job: JobCreate):
    new_id = max(job["id"] for job in jobs_seed) + 1
    new_job = job.dict()
    new_job["id"] = new_id
    jobs_seed.append(new_job)
    return new_job
