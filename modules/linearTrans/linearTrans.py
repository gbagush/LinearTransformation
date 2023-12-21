from sympy import symbols, Matrix, simplify

def is_linear_transformation(func, vars):
    v = symbols(vars)
    w = symbols([f'w{i}' for i in range(1, len(v) + 1)])
    c = symbols('c')

    u = Matrix(v)
    u_plus_w = Matrix(v) + Matrix(w)
    c_times_v = c * Matrix(v)

    T_v_plus_w = func.subs(list(zip(v, u_plus_w)))
    T_v_plus_T_w = func.subs(list(zip(v, u)))
    T_cv = func.subs(list(zip(v, w)))
    c_Tv = c * func.subs(list(zip(v, u)))

    additivity_check = simplify(T_v_plus_w - (T_v_plus_T_w + T_cv)) == Matrix([[0],[0]])
    homogeneity_check = simplify(c_Tv - func.subs(list(zip(v, c * u)))) == Matrix([[0],[0]])

    return additivity_check, homogeneity_check

def linearTrans(dim, vars, func):
    print("\nT(U + V):")
    print(func.subs(list(zip(vars, symbols(vars)))) + func.subs(list(zip(vars, symbols([f'w{i}' for i in range(1, dim + 1)])))))

    print("\nT(U) + T(V):")
    print(func.subs(list(zip(vars, symbols(vars)))) + func.subs(list(zip(vars, symbols([f'w{i}' for i in range(1, dim + 1)])))))

    print("\nT(c * V):")
    print(func.subs(list(zip(vars, symbols('c') * Matrix(symbols(vars))))))

    print("\nc * T(V):")
    print(symbols('c') * func.subs(list(zip(vars, symbols(vars)))))

    additivity_check, homogeneity_check = is_linear_transformation(func, vars)

    print("\nAdditivity Check:", additivity_check)
    print("Homogeneity Check:", homogeneity_check)

    print("\nIs T a linear transformation?", additivity_check and homogeneity_check)