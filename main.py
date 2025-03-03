import matplotlib.pyplot as plt
import numpy as np

from src.sigmoid import sigmoid             # Función sigmoidal
from src.step import step                  # Función escalón
#from src.gaussiana import gaussian            # Función gaussiana
from src.sign import sign             # Función identidad
from src.linear import linear      # Función lineal a tramos
from src.relu import relu                     # Función ReLU (Rectified Linear Unit)
#from src.sinusoidal import sinusoidal         # Función sinusoidal
from src.tahn import tanh       # Función tangente hiperbólica  

# Función para graficar funciones de activación y sus derivadas
def plot_activation_function(func, x_range, title, derivative=False, num_points=200):
    x = np.linspace(*x_range, num_points)
    y = func(x, derivative)
    plt.plot(x, y, label=title)
    plt.title(title)
    plt.xlabel("Entrada")
    plt.ylabel("Salida")
    plt.legend()
    plt.grid()

# Función principal que organiza las gráficas
def main():
    x_range = (-5, 5)
    plt.figure(figsize=(12, 8))
    
    # Graficar funciones de activación
    plt.subplot(2, 3, 1)
    plot_activation_function(sigmoid, x_range, "Sigmoid")
    plt.subplot(2, 3, 2)
    plot_activation_function(relu, x_range, "ReLU")
    plt.subplot(2, 3, 3)
    plot_activation_function(tanh, x_range, "Tanh")
    plt.subplot(2, 3, 4)
    plot_activation_function(sign, x_range, "Sign")
    plt.subplot(2, 3, 5)
    plot_activation_function(step, x_range, "Step")
    plt.subplot(2, 3, 6)
    plot_activation_function(linear, x_range, "Linear")
    
    plt.figure(figsize=(12, 4))
    
    # Graficar derivadas de funciones de activación juntas
    plt.subplot(1, 4, 1)
    plot_activation_function(sigmoid, x_range, "Sigmoid Derivative", True)
    plt.subplot(1, 4, 2)
    plot_activation_function(relu, x_range, "ReLU Derivative", True)
    plt.subplot(1, 4, 3)
    plot_activation_function(tanh, x_range, "Tanh Derivative", True)
    plt.subplot(1, 4, 4)
    plot_activation_function(linear, x_range, "Linear Derivative", True)
    
    plt.tight_layout()
    plt.show()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
