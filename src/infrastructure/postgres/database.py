from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.settings.environment import Environment
from src.patterns.singleton import Singleton


class PostgresDatabase(metaclass=Singleton):
    def __init__(self):
        self.env = Environment()
        self.__engine = self.__create_database_engine()
        self.__base = self.__create_base()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.env.POSTGRES_CONNECTION_STRING)
        return engine
    
    def __create_base(self):
        return declarative_base()

    def get_engine(self):
        return self.__engine

    def get_base(self):
        return self.__base

    def create_all_entities(self):
        self.__base.metadata.create_all(self.__engine)

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.session = None
    