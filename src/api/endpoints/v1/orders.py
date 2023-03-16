from fastapi import APIRouter
from fastapi.responses import JSONResponse

orders_router = APIRouter()

@orders_router.get("/orders/get_all_orders")
async def get_all_orders():
    return JSONResponse({"status": "Healthy"})
