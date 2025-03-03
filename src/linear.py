import numpy as np

# Función lineal: simplemente devuelve el valor de entrada
# Su derivada es siempre 1
def linear(x, derivative=False):
    if derivative:
        return np.ones_like(x)  # La derivada de una función lineal es 1
    return x
