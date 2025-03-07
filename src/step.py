import numpy as np
"""
Step function: returns 1 for values ​​>= 0 and 0 for negative values
The derivative of sign is 0 at almost all points
"""
def step(x, derivative=False):
    if derivative:
        return np.zeros_like(x)
    return np.where(x >= 0, 1, 0)