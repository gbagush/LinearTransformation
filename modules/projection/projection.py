import numpy as np

from modules.utils.vectorLength import vectorLength
from modules.utils.transpose import transpose

def projection(matrix):
    return np.divide(
        np.multiply(matrix, transpose(matrix)), (vectorLength(matrix)**2)
    )