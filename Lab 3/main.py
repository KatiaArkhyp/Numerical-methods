import numpy as np


def cubic_spline_coefficients(x_values, y_values):
    n = len(x_values)
    h = np.diff(x_values)
    alpha = np.zeros(n)
    for i in range(1, n - 1):
        alpha[i] = 3 / h[i] * (y_values[i + 1] - y_values[i]) - 3 / h[i - 1] * (y_values[i] - y_values[i - 1])
    lower = np.zeros(n)
    upper = np.zeros(n)
    z = np.zeros(n)
    lower[0] = 1
    upper[0] = z[0] = 0
    for i in range(1, n - 1):
        lower[i] = 2 * (x_values[i + 1] - x_values[i - 1]) - h[i - 1] * upper[i - 1]
        upper[i] = h[i] / lower[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / lower[i]
    lower[n - 1] = 1
    z[n - 1] = 0
    c = np.zeros(n)
    b = np.zeros(n - 1)
    d = np.zeros(n - 1)
    for j in range(n - 2, -1, -1):
        c[j] = z[j] - upper[j] * c[j + 1]
        b[j] = (y_values[j + 1] - y_values[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])
    return y_values, b, c, d, x_values


def cubic_spline_interpolation(coefficients, x_star):
    y_values, b, c, d, x_values = coefficients
    n = len(x_values)
    for i in range(n - 1):
        if x_star >= x_values[i] and x_star <= x_values[i + 1]:
            break
    y_star = y_values[i] + b[i] * (x_star - x_values[i]) + c[i] * (x_star - x_values[i]) ** 2 + d[i] * (x_star - x_values[i]) ** 3
    return y_star


x_values = np.array([0.1, 0.5, 0.9, 1.3, 1.7])
y_values = np.array([100.0, 4.0, 1.2346, 0.59172, 0.34602])
x_star = 8

coefficients = cubic_spline_coefficients(x_values, y_values)
y_star = cubic_spline_interpolation(coefficients, x_star)

print(f'f({x_star}) = {y_star}')
