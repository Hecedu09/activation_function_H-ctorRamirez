import numpy as np

# Función escalón (step): devuelve 1 para valores >= 0 y 0 para valores negativos
# Su derivada es 0 en casi todos los puntos
def step(x, derivative=False):
    if derivative:
        return np.zeros_like(x)  # Derivada es 0 en casi todos los puntos
    return np.where(x >= 0, 1, 0)