import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient    

class TestUsersV1(unittest.TestCase):
    def setUp(self):
        from src.main import app
        self.client = TestClient(app)

    def test_create_new_user(self):
        response = self.client.post("/v1/users/create")

        self.assertEqual(response.status_code, 200)