import unittest

from src.entities.users.schemas import UserRegister
from src.entities.users.services import UserService


class TestUserService(unittest.TestCase):
    def test_create_user(self):
        valid_user = UserRegister(**{
            "full_name": "Full Name",
            "email": "email@email.com",
            "cpf": "12312312312",
            "password": "password",
            "disabled": False
        })
        
        response = UserService.create_user(valid_user)

        self.assertTrue(response)