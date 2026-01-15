from fastapi import APIRouter, HTTPException
from typing import List
from models.user import User, UserCreate
from store.memory import users_seed
from services.recommendation_service import get_recommendations  # We'll use this for recommendations

router = APIRouter()


@router.get("/", response_model=list[User])
def get_users():
    return users_seed


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_seed:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    new_id = max(user["id"] for user in users_seed) + 1
    new_user = user.dict()
    new_user["id"] = new_id
    users_seed.append(new_user)
    return new_user


# Recommendation endpoint
@router.get("/{user_id}/recommendations")
def recommendations(user_id: int):
    user = None
    for u in users_seed:
        if u["id"] == user_id:
            user = u
            break
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    recommended_jobs = get_recommendations(user)
    return {"user_id": user_id, "recommended_jobs": recommended_jobs}
