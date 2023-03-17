from pydantic import BaseModel, validator

class UserRegister(BaseModel):
    full_name: str
    email: str
    cpf: str
    password: str
    disabled: bool | None = None