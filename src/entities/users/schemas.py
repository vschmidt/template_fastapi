from pydantic import BaseModel, validator

class UserSchema(BaseModel):
    full_name: str
    email: str
    cpf: str
    disabled: bool = False

    @validator("cpf")
    def cpf_have_right_len(cls, cpf):
        if len(cpf) != 11:
            raise ValueError("CPF deve conter 11 caracteres")
                
        return cpf

class UserRegisterSchema(UserSchema):
    password: str
    
class UserInDBSchema(UserSchema):
    hashed_password: str

class UserLoginSchema(BaseModel):
    email: str
    password: str