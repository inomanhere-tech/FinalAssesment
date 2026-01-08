from fastapi import APIRouter,HTTPException
from fastapi import BaseModel
import json

router = APIRouter()


## loading the job data 
def load_data():
   with open('memory.json','r') as f:
        data = json.load(f)
        return data

# showing all the users 
@router.get("/jobs")
def view():
   data = load_data()
   return data

# showing the job by id 
@router.get("/jobs/{job_id}")  ##on browser fromat to get
def view_job(job_id: str)
   
   data = load_data()  ## all data came in this and later chk spcfc

   if job_id in data:
      return data[job_id]
 
   raise HTTPException(status_code=404,detail='Incorrect way ')

@router.post("/create_jobs",response_class= JobCreate)  ##on browser fromat to get
def create_job()
   
   data = load_data()  ## all data came in this and later chk spcfc

   if job_id in data:
      return 'already exist'
 
   raise HTTPException(status_code=404,detail='Incorrect way ')
