from sympy import *
from sympy.solvers import solve
from sympy.abc import x

function = "cos(x) - x"
expr = simplify(function)
print(solve(expr, x))