
from datetime import timedelta, datetime

from passlib.context import CryptContext
from jose import jwt

from src.entities.users.schemas import UserRegisterSchema, UserInDBSchema, UserLoginSchema
from src.entities.users.repository import UserRepository
from src.shared.exceptions.exceptions import UserAlreadyExists
from src.settings.environment import Environment

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
        env = Environment()
        user_in_db = UserRepository.get_user_by_cpf(user.cpf)

        if user_in_db and cls.__verify_password(user.password, user_in_db.hashed_password):                
            access_token_expires = timedelta(minutes=env.ACCESS_TOKEN_EXPIRE_MINUTES)
            
            access_token = cls.__create_access_token(
                data={"cpf": user_in_db.cpf, "email": user_in_db.email}, 
                expires_delta=access_token_expires
            )

            return access_token
        
        return False

    @classmethod
    def __verify_password(cls, plain_password:str, hashed_password:str):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.verify(plain_password, hashed_password)
    
    @classmethod
    def __create_access_token(cls, data:dict, expires_delta:timedelta):
        env = Environment()

        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta    
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, env.SECRET_KEY, algorithm=env.ALGORITHM)
        return encoded_jwt