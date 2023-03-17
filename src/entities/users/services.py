
from src.entities.users.schemas import UserRegister
from src.entities.users.repository import UserRepository
from src.shared.exceptions.exceptions import UserAlreadyExists

class UserService:
    @classmethod
    def create_user(cls, user_to_register:UserRegister):
        user_already_in_db = UserRepository.get_user_by_cpf(user_to_register.cpf)
        if user_already_in_db:
            raise UserAlreadyExists
        
        UserRepository.create_new_user(user_to_register)

