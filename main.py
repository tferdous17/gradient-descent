import numpy as np
import matplotlib.pyplot as plt


def y_function(x):
    return np.sin(x)


def y_derivative(x):
    return np.cos(x)


x = np.arange(-5, 5, 0.1)
y = y_function(x)

current_pos = (1.5, y_function(1.5))

learning_rate = 0.01

for _ in range(1000):
    # calculates new X coord by moving us towards the local min using a negative slope (-y_derivative)
    new_x = current_pos[0] - learning_rate * y_derivative(current_pos[0])
    new_y = y_function(new_x)  # new Y coord is simply x^2
    current_pos = (new_x, new_y)  # set new current_pos per iteration

    plt.plot(x, y)
    plt.scatter(current_pos[0], current_pos[1], color="red")
    plt.pause(0.001)
    plt.clf()
