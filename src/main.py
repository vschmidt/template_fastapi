import logging
from fastapi import FastAPI

from src.api.endpoints.healthcheck import health_check_router

def inject_routers(app: FastAPI):
    app.include_router(health_check_router, tags=["HealthCheck"])


logging.info("Application starting...")

app = FastAPI()
inject_routers(app)

logging.info("Application started")