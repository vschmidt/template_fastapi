import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient


class TestOrdersV1(unittest.TestCase):
    def setUp(self):
        from src.main import app

        self.client = TestClient(app)

    @patch("src.api.endpoints.v1.orders.OrderService")
    def test_get_all_orders(self, service_mock):
        response = self.client.get("/v1/orders/get_all_orders")

        service_mock.get_all_orders.assert_called_once()
        self.assertEqual(response.status_code, 200)
