from src.core.function import Function
from .aux_funct import to_string


def bisection(f: Function, a: float, b: float, error: float):
    result: list[list] = []
    while True:
        x = (a + b) / 2.0
        real_error = (b - a) / 2
        result.append([a, b, x, real_error])
        print(f"{a}   {b}   {x}   {real_error}")
        if f.get_y(x) == 0:
            break
        if f.get_y(a) * f.get_y(x) < 0:
            b = x
        else:
            a = x
        if real_error < error:
            break
    to_string(result)
    return {
        "headers": ["a", "b", "x", "error"],
        "content": result
    }
