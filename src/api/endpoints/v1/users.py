import logging
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.entities.users.schemas import UserRegisterSchema
from src.entities.users.services import UserService

users_router = APIRouter()

@users_router.post("/users/create")
async def get_all_orders(user: UserRegisterSchema):
    try:
        UserService.create_user(user)
        return JSONResponse({"message":"Usuário criado"}, status_code=status.HTTP_201_CREATED)
    except Exception as err:
        logging.error(err)
        return JSONResponse({"message":"Erro ao processar"}, status_code=status.HTTP_400_BAD_REQUEST)

    
