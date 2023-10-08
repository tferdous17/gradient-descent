import numpy as np
import matplotlib.pyplot as plt


def z_function(x, y):
    # fancy wave function
    return np.sin(5 * x) * np.cos(5 * y) / 5


def calculate_gradient(x, y):
    return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)