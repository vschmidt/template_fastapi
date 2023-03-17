from sqlalchemy import insert, select

from src.entities.users.models import UserModel
from src.entities.users.schemas import UserRegister
from src.infrastructure.postgres.database import PostgresDatabase

class UserRepository:
    @classmethod
    def create_new_user(cls, user:UserRegister):
        with PostgresDatabase() as engine:
            engine.session.execute(insert(user))
            engine.session.commit()

    @classmethod
    def get_user_by_cpf(cls, cpf:str) -> UserRegister:
        with PostgresDatabase() as engine:
            result = engine.session.execute(select(UserModel).where(UserModel.cpf==cpf))
        
        if result:
            return UserRegister(**result.to_dict())        
        return None