from fastapi import FastAPI
from app.routes import health, jobs, users
import uvicorn
app = FastAPI(title="Job Recommendation API")

app.include_router(health.router)
app.include_router(jobs.router, prefix="/jobs")
app.include_router(users.router, prefix="/users")
