from fastapi import Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasicCredentials
from src.schemas.petition import PetitionBase
from src.core.algotithms.bisection import bisection
from src.core.algotithms.regula_falsi import regula_falsi
from src.core.algotithms.secantes import secantes
from src.core.function import Function
from src.core.algotithms.newton_raphson import newton_raphson
from src.router.core_router import CoreRoutes
import json


class ConversationRoutes(CoreRoutes):
    def init_routes(self):
        @self.router.get(self.prefix + "/bisection")
        async def bisection_algorithm(algorithm: int, func: str, a: float, b: float, error: float):
            if algorithm < 0 or algorithm > 3:
                return JSONResponse(
                    status_code=300,
                    content="Invalid parameter algorithm"
                )
            function = Function(func)
            algotithm_to_use = bisection
            if algorithm == 0:
                algotithm_to_use = bisection
            elif algorithm == 1:
                algotithm_to_use = regula_falsi
            elif algorithm == 2:
                algotithm_to_use = newton_raphson
            elif algorithm == 3:
                algotithm_to_use = secantes
            return JSONResponse(
                status_code=200,
                content=algotithm_to_use(function, a, b, error)
            )
