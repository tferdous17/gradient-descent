import numpy as np
import matplotlib.pyplot as plt


def z_function(x, y):
    # fancy wave function
    return np.sin(5 * x) * np.cos(5 * y) / 5


def calculate_gradient(x, y):
    # calculate derivatives of x, y
    return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)


x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)

Z = z_function(X, Y)

current_pos = (0.7, 0.4, z_function(0.7, 0.4))
learning_rate = 0.01

ax = plt.subplot(projection='3d')

for _ in range(1000):
    X_derivative, Y_derivative = calculate_gradient(current_pos[0], current_pos[1])
    X_new, Y_new = current_pos[0] - learning_rate * X_derivative, current_pos[1] - learning_rate * Y_derivative
    current_pos = (X_new, Y_new, z_function(X_new, Y_new))

    ax.plot_surface(X, Y, Z, cmap="viridis")

