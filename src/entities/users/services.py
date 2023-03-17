
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
        user_in_db = UserRepository.get_user_by_cpf(user.cpf)

        if user_in_db and cls.verify_password(user.password, user_in_db.hashed_password):                
            return "mylittleponey"
        
        return False

    @classmethod
    def verify_password(cls, plain_password:str, hashed_password:str):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.verify(plain_password, hashed_password)