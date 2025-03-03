import numpy as np

# Función sigmoide: usada comúnmente en redes neuronales para mapear valores entre 0 y 1
# Su derivada es útil para el retropropagación en aprendizaje profundo
def sigmoid(x, derivative=False):
    sig = 1 / (1 + np.exp(-x))
    if derivative:
        return sig * (1 - sig)
    return sig