import logging
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.entities.users.schemas import UserRegisterSchema, UserLoginSchema
from src.entities.users.services import UserService

users_router = APIRouter()

@users_router.post("/users/create")
async def create_user(user: UserRegisterSchema):
    try:
        UserService.create_user(user)
        return JSONResponse({"message":"Usuário criado"}, status_code=status.HTTP_201_CREATED)
    except Exception as err:
        logging.error(err)
        return JSONResponse({"message":"Erro ao processar"}, status_code=status.HTTP_400_BAD_REQUEST)

@users_router.post("/users/token")
async def get_user_token(user: UserLoginSchema):
    try:
        jwt_token_created = UserService.token_login(user)

        if jwt_token_created:            
            return JSONResponse({"access_token": jwt_token_created, "token_type": "bearer"},
                                status_code=status.HTTP_200_OK)

        return JSONResponse({"message":"CPF ou senha inválido(s)"}, status_code=status.HTTP_401_UNAUTHORIZED)
    except Exception as err:
        logging.error(err)
        return JSONResponse({"message":"Erro ao processar"}, status_code=status.HTTP_400_BAD_REQUEST)

    

