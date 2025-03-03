import numpy as np

def tanh(x, derivative=False):
    if derivative:
        return 1 - np.tanh(x) ** 2
    return np.tanh(x)