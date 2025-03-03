import numpy as np

# Función signo: devuelve -1, 0 o 1 dependiendo del signo del valor de entrada
# Su derivada es 0 en casi todos los puntos, excepto en discontinuidades
def sign(x, derivative=False):
    if derivative:
        return np.zeros_like(x)  # La derivada de sign es 0 en casi todos los puntos
    return np.sign(x)