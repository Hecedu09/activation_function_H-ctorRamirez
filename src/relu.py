import numpy as np
"""
ReLU (Rectified Linear Unit) function: allows positive values to pass and blocks negative ones.
Its derivative is 1 for positive values and 0 for negative values."
"""
def relu(x, derivative=False):
    if derivative:
        return np.where(x > 0, 1, 0)  # ReLU derivative
    return np.maximum(0, x)
