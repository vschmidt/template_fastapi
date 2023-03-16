from fastapi import APIRouter

from src.entities.orders.services import OrderService

orders_router = APIRouter()

@orders_router.get("/orders/get_all_orders")
async def get_all_orders():
    return OrderService.get_all_orders()
