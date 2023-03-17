import pytest
import unittest
from unittest.mock import patch
from datetime import datetime

from src.entities.orders.schemas import CreateOrderSchema
from src.entities.orders.services import OrderService


@patch("src.entities.orders.services.OrderRepository")
class TestUserService(unittest.TestCase):
    def test_create_user(self, repository_mock):
        order = CreateOrderSchema(
            **{
                "code": 1589,
                "value": 22.5,
                "cpf": "12345645600",
                "date": str(datetime.utcnow()),
            }
        )
        repository_mock.create_new_order.return_value = None

        response = OrderService.create_order(order)

        self.assertIsNone(response)

        repository_mock.create_new_order.assert_called_once_with(order)
