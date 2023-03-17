from fastapi import APIRouter, Depends

from src.entities.orders.schemas import CreateOrderSchema
from src.entities.orders.services import OrderService
from src.shared.auth_bearer_validator import AuthBearerValidator

orders_router = APIRouter()


@orders_router.get("/orders/get_all_orders")
async def get_all_orders(token_infos: dict = Depends(AuthBearerValidator())):
    return OrderService.get_all_orders()


@orders_router.post("/orders/create")
async def create_order(
    order: CreateOrderSchema, token_infos: dict = Depends(AuthBearerValidator())
):
    return OrderService.create_order(order)
