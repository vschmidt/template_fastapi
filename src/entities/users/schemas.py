from pydantic import BaseModel, validator

class UserRegisterSchema(BaseModel):
    full_name: str
    email: str
    cpf: str
    password: str
    disabled: bool = False

    @validator("cpf")
    def cpf_have_right_len(cls, cpf):
        if len(cpf) != 11:
            raise ValueError("CPF deve conter 11 caracteres")
                
        return cpf
