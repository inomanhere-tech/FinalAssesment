from fastapi import FastAPI
from routes import health, jobs, users
import uvicorn
app = FastAPI(title="Job Recommendation API")

app.include_router(health.router)
app.include_router(jobs.router, prefix="/jobs")
app.include_router(users.router, prefix="/users")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
