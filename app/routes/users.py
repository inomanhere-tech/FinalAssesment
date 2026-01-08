from fastapi import APIRouter,HTTPException

router = APIRouter()

## loading the suers data 
def load_data():
   with open('memory.json','r') as f:
        data = json.load(f)
        return data

# showing all the users 
@router.get("/users")
def view():
   data = load_data()
   return data

# showing the user by id 
@router.get("/users/{user_id}")  ##on browser fromat to get
def view_user(user_id: str)
   
   data = load_data()  ## all data came in this and later chk spcfc

   if user_id in data:
      return data[user_id]
 
   raise HTTPException(status_code=404,detail='The entered usert not found')

@router.post("/create_user",response_model="UserCreate")  ##on browser fromat to get
def create_user():
   
   data = load_data()  ## all data came in this and later chk spcfc

   if user_id not in data:
        data["user_id"]= data["user_id"].append()
      
    raise "Already existed"
 
