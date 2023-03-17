
from passlib.context import CryptContext

from src.entities.users.schemas import UserRegisterSchema, UserInDBSchema, UserLoginSchema
from src.entities.users.repository import UserRepository
from src.shared.exceptions.exceptions import UserAlreadyExists

class UserService:
    @classmethod
    def create_user(cls, user_to_register:UserRegisterSchema):
        user_already_in_db = UserRepository.get_user_by_cpf(user_to_register.cpf)
        if user_already_in_db:
            raise UserAlreadyExists
        
        user_to_register = cls.__encripty_user_password(user_to_register)
        UserRepository.create_new_user(user_to_register)

    @classmethod
    def __encripty_user_password(cls, user:UserRegisterSchema) -> UserInDBSchema:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        user_hashed_password = {"hashed_password":pwd_context.hash(user.password)}
    
        user_hashed_password.update(user.dict())
        user_with_hased_pass = UserInDBSchema(**user_hashed_password)

        return user_with_hased_pass

    @classmethod
    def token_login(cls, user:UserLoginSchema):
        return None
