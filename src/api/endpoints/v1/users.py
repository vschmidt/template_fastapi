from fastapi import APIRouter

from src.entities.users.schemas import UserRegister

users_router = APIRouter()

@users_router.post("/users/create")
async def get_all_orders(user: UserRegister):
    pass
