import unittest
from unittest.mock import patch

from src.entities.users.schemas import UserRegister


class TestUserSchemas(unittest.TestCase):
    def test_user_register(self):
        valid_user = UserRegister(**{
            "full_name": "Full Name",
            "email": "email@email.com",
            "cpf": "12312312312",
            "password": "password",
            "disabled": False
        })

        self.assertEqual(len(valid_user.dict().keys()), 5)