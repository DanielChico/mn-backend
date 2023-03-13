from abc import ABC, abstractmethod

from fastapi import APIRouter
from fastapi.security import HTTPBasic

from src.config.config import Config


class CoreRoutes(ABC):
    router: APIRouter
    security: HTTPBasic
    api_version: str
    prefix: str

    def __init__(self, router: APIRouter, prefix: str, security: HTTPBasic):
        self.router = router
        self.security = security
        self.api_version = Config.API_VERSION
        self.prefix = prefix

    @abstractmethod
    def init_routes(self):
        pass
