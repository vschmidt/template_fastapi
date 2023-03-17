import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient    

from src.entities.users.schemas import UserRegister

class TestUsersV1(unittest.TestCase):
    def setUp(self):
        from src.main import app
        self.client = TestClient(app)
    
    @patch("src.api.endpoints.v1.users.UserService")
    def test_create_new_user(self, service_mock):
        user = UserRegister(**{
            "full_name": "Full Name",
            "email": "email@email.com",
            "cpf": "12312312312",
            "password": "password",
            "disabled": False
        }).dict()

        response = self.client.post("/v1/users/create", json=user)

        self.assertEqual(response.status_code, 200)
        service_mock.create_user.assert_called_once()