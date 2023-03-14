from src.core.function import Function
from .aux_funct import to_string


def secantes(f: Function, a: float, b: float, error: float):
    result: list[list] = []
    ya = f.get_y(a)
    yb = f.get_y(b)
    while True:
        xc = b - ((b - a) / (yb - ya) * yb)
        yc = f.get_y(xc)
        actual_error = abs(xc - b)
        result.append([a, b, xc, actual_error])
        a = b
        b = xc
        ya = yb
        yb = yc
        if actual_error < error:
            break
    to_string(result)
    return {
        "headers": ["a", "b", "x", "error"],
        "content": result
    }
