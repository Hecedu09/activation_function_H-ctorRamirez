import matplotlib.pyplot as plt
import numpy as np

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from scr import train_neural_network
from scr import sigmoid
from scr import relu

def plot_sigmoid():
    x = np.linspace(-10, 10, 100)
    y = sigmoid(x)
    
    plt.plot(x, y, label="Sigmoid")
    plt.title("Función Sigmoide")
    plt.legend()
    plt.grid()
    plt.show()

def plot_relu():
    x = np.linspace(-10, 10, 100)
    y = relu(x)

    plt.plot(x, y, label="ReLU")
    plt.title("Función ReLU")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_sigmoid()
    plot_relu()
    train_neural_network()