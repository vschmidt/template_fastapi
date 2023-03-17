from src.entities.orders.repository import OrderRepository


class OrderService:
    @classmethod
    def get_all_orders(cls):
        return OrderRepository.get_all_orders()
