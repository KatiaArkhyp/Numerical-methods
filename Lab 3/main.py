import numpy as np


def cubic_spline_coefficients(x, f):
    n = len(x)
    h = np.diff(x)
    alpha = np.zeros(n)
    for i in range(1, n - 1):
        alpha[i] = 3 / h[i] * (f[i + 1] - f[i]) - 3 / h[i - 1] * (f[i] - f[i - 1])
    l = np.zeros(n)
    mu = np.zeros(n)
    z = np.zeros(n)
    l[0] = 1
    mu[0] = z[0] = 0
    for i in range(1, n - 1):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]
    l[n - 1] = 1
    z[n - 1] = 0
    c = np.zeros(n)
    b = np.zeros(n - 1)
    d = np.zeros(n - 1)
    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (f[j + 1] - f[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])
    return f, b, c, d, x


def cubic_spline_interpolation(coefficients, x_star):
    f, b, c, d, x = coefficients
    n = len(x)
    for i in range(n - 1):
        if x_star >= x[i] and x_star <= x[i + 1]:
            break
        y_star = f[i] + b[i] * (x_star - x[i]) + c[i] * (x_star - x[i]) ** 2 + d[i] * (x_star - x[i]) ** 3
    return y_star


x = np.array([0.1, 0.5, 0.9, 1.3, 1.7])
f = np.array([100.0, 4.0, 1.2346, 0.59172, 0.34602])
x_star = 8

coefficients = cubic_spline_coefficients(x, f)
y_star = cubic_spline_interpolation(coefficients, x_star)

print(f'f({x_star}) = {y_star}')
