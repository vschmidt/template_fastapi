from datetime import datetime
from typing import Optional

from pydantic import Field, BaseModel, validator


class CreateOrderSchema(BaseModel):
    code: int = Field(example=1589)
    value: float = Field(example=22.5)
    cpf: str = Field(max_length=11, example="12345645600")
    date: str = Field(example=datetime.now(), default=datetime.now())

    @validator("cpf")
    def cpf_have_right_len(cls, cpf):
        if len(cpf) != 11:
            raise ValueError("CPF deve conter 11 caracteres")

        return cpf


class OrderSchema(BaseModel):
    code: int = Field(example=1589)
    value: float = Field(example=22.5)
    cpf: str = Field(max_length=11, example="12345645600")
    date: str = Field(example=datetime.now(), default=datetime.now())
    status: Optional[str] = Field(example="In validation")
    created_at: str = Field(example=datetime.now(), default=datetime.now())
    updated_at: str = Field(example=datetime.now(), default=datetime.now())

    @validator("cpf")
    def cpf_have_right_len(cls, cpf):
        if len(cpf) != 11:
            raise ValueError("CPF deve conter 11 caracteres")

        return cpf
