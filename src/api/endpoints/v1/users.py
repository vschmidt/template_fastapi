from fastapi import APIRouter

from src.entities.users.schemas import UserRegister
from src.entities.users.services import UserService

users_router = APIRouter()

@users_router.post("/users/create")
async def get_all_orders(user: UserRegister):
    UserService.create_user(user)
