from sympy import *
from sympy.abc import x

class Function:
    def __init__(self, function: str):
        self.expression = simplify(function)
        self.str_function = function

    def get_y(self, value: float):
        result = self.expression.subs(x, value)
        return result
