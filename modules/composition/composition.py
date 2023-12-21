import numpy as np
from modules.linearTransAsMatrices.linearTransAsMatrices import linearTransAsMatrices

def evaluateComposition(SSize, SFunction, TSize, TFunction):
    S = linearTransAsMatrices("S", SSize, SFunction)
    print(S)

    T = linearTransAsMatrices("T", TSize, TFunction)
    print(T)

    print("(S◦T)")

    return np.dot(S, T)