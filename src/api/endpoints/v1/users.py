from fastapi import APIRouter

users_router = APIRouter()

@users_router.post("/users/create")
async def get_all_orders():
    pass
