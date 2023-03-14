from src.core.function import Function
from .aux_funct import to_string
from sympy import diff
from sympy.abc import x


def newton_raphson(f: Function, a: float, b: float, error: float):
    derivative = diff(f.expression, x)
    result: list[list] = []
    xa = select_x(f, derivative, a, b)
    first_iter = True
    while True:
        xi = xa - (f.get_y(xa)/derivative.subs(x, xa))
        if first_iter:
            actual_error = (b - a) / 2
            first_iter = False
        else:
            actual_error = abs(xi - xa)
        result.append([a, b, xi, actual_error])
        print(f"{a}   {b}   {xi}   {actual_error}")
        xa = xi
        if actual_error < error:
            break
    to_string(result)
    return {
        "headers": ["a", "b", "x", "error"],
        "content": result
    }


def select_x(f: Function, derivative, a: float, b: float):
    if f.get_y(a) * derivative.subs(x, a) > 0:
        return a
    return b
