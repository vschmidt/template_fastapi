"""
Order repository module
"""
from sqlalchemy import select

from src.entities.orders.models import OrderModel
from src.entities.orders.schemas import OrderSchema
from src.infrastructure.postgres.database import PostgresDatabase

class OrderRepository:
    @classmethod
    def get_all_orders(cls):
        with PostgresDatabase() as engine:
            results = engine.session.execute(select(OrderModel)).all()

        results = [OrderSchema(**r[0].to_dict()) for r in results]
        return results
