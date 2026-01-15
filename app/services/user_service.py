from store import memory
from models.user import User, UserCreate


def get_all_users():
    return memory.users


def get_user_by_id(user_id: int):
    for user in memory.users:
        if user.user_id == user_id:
            return user
    return None


def create_user(user: UserCreate):
    new_id = len(memory.users) + 1
    new_user = User(user_id=new_id, **user.dict())
    memory.users.append(new_user)
    return new_user
