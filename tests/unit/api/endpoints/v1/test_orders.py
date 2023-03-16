import unittest
from fastapi.testclient import TestClient    

class TestOrdersV1(unittest.TestCase):
    def setUp(self):
        from src.main import app
        self.client = TestClient(app)

    def test_get_all_orders(self):
        response = self.client.get("/v1/orders/get_all_orders")

        self.assertEqual(response.status_code, 200)