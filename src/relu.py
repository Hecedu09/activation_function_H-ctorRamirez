import numpy as np

# Función ReLU (Rectified Linear Unit): permite el paso de valores positivos y bloquea los negativos
# Su derivada es 1 para valores positivos y 0 para valores negativos
def relu(x, derivative=False):
    if derivative:
        return np.where(x > 0, 1, 0)  # Derivada de ReLU
    return np.maximum(0, x)