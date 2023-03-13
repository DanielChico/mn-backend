from src.core.function import Function
from sympy import diff
from sympy.abc import x


def val_bolsano(f: Function, a: int, b: int):
    return f.get_y(a) * f.get_y(b) < 0

def val_cambio_signo_primera_derivada(f: Function, a: int, b: int):
    derivate = diff(f.expression, x)
    


def to_string(result_list: list[list]):
    for i in range(len(result_list)):
        for j in range(len(result_list[i])):
            result_list[i][j] = str(round(result_list[i][j], 8))
