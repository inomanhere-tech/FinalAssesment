from fastapi import APIRouter

router = APIRouter()

from fastapi import APIRouter


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

# showing the user by id 
@router.get("/jobs/{job_id}")  ##on browser fromat to get
def view_user(job_id: str)
   
   data = load_data()  ## all data came in this and later chk spcfc

   if job_id in data:
      return data[job_id]
 
   raise HTTPException(status_code=404,detail='Incorrect way ')
