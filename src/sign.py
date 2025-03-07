import numpy as np
"""
Sign function: returns -1, 0 or 1 depending on the sign of the input value
Its derivative is 0 at almost all points, except at discontinuities
"""
def sign(x, derivative=False):
    if derivative:
        return np.zeros_like(x)
    return np.sign(x)