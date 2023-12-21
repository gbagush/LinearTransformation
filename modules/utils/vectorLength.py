import math

def vectorLength(vector):
    sum = 0

    for i in range(len(vector[0])):
        sum += vector[0][i] ** 2
    
    return math.sqrt(sum)