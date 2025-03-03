import numpy as np

# Función tangente hiperbólica: mapea valores entre -1 y 1, útil para redes neuronales
# Su derivada se calcula como 1 - tanh^2(x)
def tanh(x, derivative=False):
    if derivative:
        return 1 - np.tanh(x) ** 2
    return np.tanh(x)