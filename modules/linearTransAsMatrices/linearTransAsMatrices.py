import numpy as np
import sympy as sp

def linearTransAsMatrices(symbol, vsize, function):
    identity = np.identity(vsize)
    variable_mapping = {}
    matrix = []

    variables = [sp.Symbol(f'v{i+1}') for i in range(vsize)]

    for i in range(vsize):
        print(f"e{i+1}")
        for j in range(vsize):
            variable_mapping[variables[j]] = identity[i][j]

        for k in function:
            k_expr = sp.sympify(k)
            k_with_values = k_expr.subs(variable_mapping)
            k_eval = k_with_values.evalf()
            print(f"{symbol}(e{i+1}): {k} = {k_eval}")
            matrix.append(k_eval)

    matrix = np.array(matrix).reshape(len(function), vsize)
    return matrix