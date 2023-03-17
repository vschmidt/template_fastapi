import pytest
import unittest
from unittest.mock import patch
from datetime import datetime

from src.entities.orders.schemas import CreateOrderSchema, OrderSchema
from src.entities.orders.services import OrderService


@patch("src.entities.orders.services.OrderRepository")
class TestUserService(unittest.TestCase):
    def test_create_order(self, repository_mock):
        order = CreateOrderSchema(
            **{
                "code": 1589,
                "value": 22.5,
                "cpf": "12345645600",
                "date": str(datetime.utcnow()),
            }
        )
        order_to_save = OrderSchema(**order.dict())
        order_to_save.status = "Em validação"

        repository_mock.create_new_order.return_value = None

        response = OrderService.create_order(order)

        self.assertIsNone(response)

        repository_mock.create_new_order.assert_called_once_with(order_to_save)

    def test_create_order_with_auto_approval(self, repository_mock):
        order = CreateOrderSchema(
            **{
                "code": 1589,
                "value": 22.5,
                "cpf": "15350946056",
                "date": str(datetime.utcnow()),
            }
        )
        order_to_save = OrderSchema(**order.dict())
        order_to_save.status = "Aprovado"

        repository_mock.create_new_order.return_value = None

        response = OrderService.create_order(order)

        self.assertIsNone(response)

        repository_mock.create_new_order.assert_called_once_with(order_to_save)
