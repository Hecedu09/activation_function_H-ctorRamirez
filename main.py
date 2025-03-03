import matplotlib.pyplot as plt
import numpy as np

from src.sigmoid import sigmoid             # Función sigmoidal
#from src.escalon import step                  # Función escalón
#from src.gaussiana import gaussian            # Función gaussiana
#from src.identity import identity             # Función identidad
#from src.lineal_a_tramos import piecewise       # Función lineal a tramos
from src.relu import relu                     # Función ReLU (Rectified Linear Unit)
#from src.sinusoidal import sinusoidal         # Función sinusoidal
from src.tahn import tanh       # Función tangente hiperbólica  

def plot_activation_function(func, x_range, title):
    x = np.linspace(*x_range, 100)
    y = func(x)
    plt.plot(x, y, label=title)
    plt.title(title)
    plt.xlabel("Entrada")
    plt.ylabel("Salida")
    plt.legend()
    plt.grid()

def main():
    x_range = (-5, 5)
    plt.figure(figsize=(10, 6))
    
    plt.subplot(1, 3, 1)
    plot_activation_function(sigmoid, x_range, "Sigmoid")
    
    plt.subplot(1, 3, 2)
    plot_activation_function(relu, x_range, "ReLU")
    
    plt.subplot(1, 3, 3)
    plot_activation_function(tanh, x_range, "Tanh")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()