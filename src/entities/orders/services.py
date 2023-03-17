from src.entities.orders.repository import OrderRepository
from src.entities.orders.schemas import CreateOrderSchema, OrderSchema
from src.settings.environment import Environment


class OrderService:
    @classmethod
    def get_all_orders(cls):
        return OrderRepository.get_all_orders()

    @classmethod
    def create_order(cls, order: CreateOrderSchema):
        order_to_save = OrderSchema(**order.dict())

        if cls.__is_auto_aproved(order):
            order_to_save.status = "Aprovado"

        return OrderRepository.create_new_order(order_to_save)

    @classmethod
    def __is_auto_aproved(cls, order):
        env = Environment()
        return order.cpf in env.AUTO_APPROVED_CPFS
