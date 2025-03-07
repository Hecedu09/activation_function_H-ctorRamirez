import numpy as np

"""
Linear function: simply returns the input value.
Its derivative is always 1.
"""
def linear(x, derivative=False):
    if derivative:
        return np.ones_like(x)  # The derivative of a linear function is 1
    return x
