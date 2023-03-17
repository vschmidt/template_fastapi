from fastapi import status
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient

from tests.utils.bearer_token_utils import JWTGenerator


class TestOrdersV1(unittest.TestCase):
    def setUp(self):
        from src.main import app

        self.client = TestClient(app)
        self.jwt_generator = JWTGenerator()

    def test_get_all_orders_without_token(self):
        response = self.client.get("/v1/orders/get_all_orders")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @patch("src.api.endpoints.v1.orders.OrderService")
    def test_get_all_orders_with_valid_token(self, service_mock):
        response = self.client.get(
            "/v1/orders/get_all_orders",
            headers={
                "Authorization": f"Bearer {self.jwt_generator.generate_valid_token()}"
            },
        )

        service_mock.get_all_orders.assert_called_once()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
