from pydantic import BaseSettings, Field


class Environment(BaseSettings):
    DATABASE_CONNECTION_STRING: str = Field("postgresql+psycopg2://postgres:postgres@postgres/postgres", env="DATABASE_CONNECTION_STRING")
