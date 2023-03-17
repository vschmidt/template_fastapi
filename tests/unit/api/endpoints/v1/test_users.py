import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient    
from fastapi import status

from src.entities.users.schemas import UserLoginSchema, UserRegisterSchema

class TestUsersV1(unittest.TestCase):
    def setUp(self):
        from src.main import app
        self.client = TestClient(app)
    
    @patch("src.api.endpoints.v1.users.UserService")
    def test_create_new_user_with_success(self, service_mock):
        user = UserRegisterSchema(**{
            "full_name": "Full Name",
            "email": "email@email.com",
            "cpf": "12312312312",
            "password": "password",
            "disabled": False
        }).dict()

        response = self.client.post("/v1/users/create", json=user)

        self.assertEqual(response.status_code, 201)
        service_mock.create_user.assert_called_once()

    @patch("src.api.endpoints.v1.users.UserService")
    def test_create_new_user_with_fail(self, service_mock):
        user = UserRegisterSchema(**{
            "full_name": "Full Name",
            "email": "email@email.com",
            "cpf": "12312312312",
            "password": "password",
            "disabled": False
        }).dict()

        service_mock.create_user.side_effect = ValueError

        response = self.client.post("/v1/users/create", json=user)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        service_mock.create_user.assert_called_once()

    @patch("src.api.endpoints.v1.users.UserService")
    def test_create_new_user_with_success(self, service_mock):
        user = UserLoginSchema(**{            
            "email": "email@email.com",           
            "password": "password",
        }).dict()
        service_mock.token_login.return_value = None

        response = self.client.post("/v1/users/token", json=user)

        self.assertEqual(response.status_code, 200)
        service_mock.token_login.assert_called_once_with(user)