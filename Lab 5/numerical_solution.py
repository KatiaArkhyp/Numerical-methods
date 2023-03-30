import numpy as np


def euler(f, a, b, y0, h):
    n = int((b - a) / h)
    x = np.linspace(a, b, n + 1)
    y = np.zeros((n + 1, len(y0)))
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + h * np.array(f(x[i], y[i]))
    return x, y


def euler_c(f, a, b, y0, h):
    n = int((b - a) / h)
    x = np.linspace(a, b, n + 1)
    y = np.zeros((n + 1, len(y0)))
    y[0] = y0
    for i in range(n):
        y_half = y[i] + (h / 2) * np.array(f(x[i], y[i]))
        y[i + 1] = y[i] + h * np.array(f(x[i] + h / 2, y_half))
    return x, y


def runge_kutta(f, a, b, y0, h):
    n = int((b - a) / h)
    x = np.linspace(a, b, n + 1)
    y = np.zeros((n + 1, len(y0)))
    y[0] = y0
    for i in range(n):
        k1 = h * np.array(f(x[i], y[i]))
        k2 = h * np.array(f(x[i] + h / 2, y[i] + k1 / 2))
        k3 = h * np.array(f(x[i] + h / 2, y[i] + k2 / 2))
        k4 = h * np.array(f(x[i] + h, y[i] + k3))
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x, y


def median_error(error_e, error_ec, error_rk):
    return (error_e + error_ec + error_rk) / 3
