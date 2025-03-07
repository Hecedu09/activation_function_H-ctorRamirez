import matplotlib.pyplot as plt
import numpy as np

from src.sigmoid import sigmoid             # Sigmoid function
from src.step import step                   # Step function
from src.sign import sign                   # Sign function
from src.linear import linear               # Linear function
from src.relu import relu                    # ReLU function
from src.tahn import tanh                    # Hyperbolic tangent function  

# Function to plot activation functions and their derivatives
def plot_activation_function(func, x_range, title, derivative=False, num_points=200):
    x = np.linspace(*x_range, num_points)
    y = func(x, derivative)
    plt.plot(x, y, label=title)
    plt.title(title)
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.legend()
    plt.grid()

# Main function that organizes the plots
def main():
    x_range = (-5, 5)
    plt.figure(figsize=(12, 8))
    
    # Plot activation functions
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
    
    # Plot activation function derivatives together
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

# Program entry point
if __name__ == "__main__":
    main()
