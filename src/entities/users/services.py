
from src.entities.users.schemas import UserRegister
from src.entities.users.repository import UserRepository
from src.shared.exceptions.exceptions import UserAlreadyExists

class UserService:
    @classmethod
    def create_user(cls, user:UserRegister):
        user = UserRepository.get_user_by_cpf(user.cpf)
        if user:
            raise UserAlreadyExists

        # insert new user


        return True

