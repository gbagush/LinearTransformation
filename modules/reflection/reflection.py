import numpy as np

from modules.utils.vectorLength import vectorLength
from modules.utils.transpose import transpose

def reflection(matrix):
    return np.subtract(
        np.divide(
            np.dot(2, np.multiply(matrix, transpose(matrix))),
            (vectorLength(matrix) ** 2)
        ),
        np.identity(len(matrix[0]))
    )
