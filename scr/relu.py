import numpy as np

def relu(x, derivative=False):
    if derivative:
        x[x <= 0] = 0
        x[x > 0] = 1
        return x
    return np.maximum(0, x)