from fastapi import APIRouter
from fastapi.security import HTTPBasic

from src.config.config import Config
from src.router.v1 import approach_algorithms_routes

router = APIRouter(prefix=Config.API_PREFIX)
security = HTTPBasic()

approach_algorithms_routes.ConversationRoutes(router, "/algorithms", security).init_routes()
