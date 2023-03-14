from src.core.function import Function
from .aux_funct import to_string


def regula_falsi(f: Function, a: float, b: float, error: float):
    result: list[list] = []
    xa = 0
    first_iter = True
    while True:
        x = a - ((b - a) / (f.get_y(b) - f.get_y(a))) * f.get_y(a)
        if first_iter:
            actual_error = (b - a) / 2
            first_iter = False
        else:
            actual_error = abs(x - xa)
        result.append([a, b, x, actual_error])
        print(f"{a}   {b}   {x}   {actual_error}")
        if f.get_y(a) * f.get_y(x) < 0:
            b = x
        else:
            a = x
        xa = x
        if actual_error < error:
            break
    to_string(result)
    return {
        "headers": ["a", "b", "x", "error"],
        "content": result
    }
