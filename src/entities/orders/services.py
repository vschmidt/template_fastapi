from src.entities.orders.repository import OrderRepository
from src.entities.orders.schemas import CreateOrderSchema


class OrderService:
    @classmethod
    def get_all_orders(cls):
        return OrderRepository.get_all_orders()

    @classmethod
    def create_order(cls, order: CreateOrderSchema):
        return OrderRepository.create_new_order(order)
