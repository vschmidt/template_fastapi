from datetime import datetime
from typing import Optional

from pydantic import Field, validator, BaseModel, root_validator

from src.settings.environment import Environment


class OrderSchema(BaseModel):
    code: int = Field(example=1589)
    value: float = Field(example=22.5)
    cpf: str = Field(max_length=11, example="12345645600")
    date: datetime = Field(example=datetime.now(), default=datetime.now())
    status: Optional[str] = Field(example="In validation")
    created_at: datetime = Field(example=datetime.now(), default=datetime.now())
    updated_at: datetime = Field(example=datetime.now(), default=datetime.now())
