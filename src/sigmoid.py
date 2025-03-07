import numpy as np
"""
Sigmoid function: commonly used in neural networks to map values between 0 and 1.
Its derivative is useful for backpropagation in deep learning."
"""
def sigmoid(x, derivative=False):
    sig = 1 / (1 + np.exp(-x))
    if derivative:
        return sig * (1 - sig)
    return sig
