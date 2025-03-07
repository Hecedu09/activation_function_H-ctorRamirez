import numpy as np
"""
Hyperbolic tangent function: maps values ​​between -1 and 1, useful for neural networks
Its derivative is calculated as 1 - tanh^2(x)
"""
def tanh(x, derivative=False):
    if derivative:
        return 1 - np.tanh(x) ** 2
    return np.tanh(x)