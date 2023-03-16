from pydantic import BaseSettings, Field


class Environment(BaseSettings):
    POSTGRES_CONNECTION_STRING: str = Field("postgresql+psycopg2://postgres:postgres@postgres/template_fastapi", env="POSTGRES_CONNECTION_STRING")
