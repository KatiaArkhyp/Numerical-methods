import numpy as np
import matplotlib.pyplot as plt
from numerical_solution import euler, euler_c, runge_kutta, median_error


def y_exact(x):
    return x ** 2 + x + 1 / x


def f(x, y):
    y1, y2 = y
    return [y2, (y1 + 3 * x ** 2 - x * y2) / x ** 2]


a, b, h = 1, 2, 0.1
y0 = [3, 2]

x_e, y_e = euler(f, a, b, y0, h)
x_ec, y_ec = euler_c(f, a, b, y0, h)
x_rk, y_rk = runge_kutta(f, a, b, y0, h)

y_exact_vals = y_exact(x_e)

print("{:^6} {:^15} {:^15} {:^15} {:^15} {:^15}".format("x", "Euler", "Euler-Cauchy", "Runge-Kutta", "Exact", "Error"))

for i in range(len(x_e)):
    error_e = abs(y_e[i][0] - y_exact_vals[i])
    error_ec = abs(y_ec[i][0] - y_exact_vals[i])
    error_rk = abs(y_rk[i][0] - y_exact_vals[i])
    print("{:^6.1f} {:^15.6f} {:^15.6f} {:^15.6f} {:^15.6f} {:^15.6f}"
          .format(x_e[i], y_e[i][0], y_ec[i][0], y_rk[i][0], y_exact_vals[i],
                  median_error(error_e, error_ec, error_rk)))

x_exact = np.linspace(1, 2, 101)
y_exact_vals = y_exact(x_exact)
plt.plot(x_e, y_e[:, 0], 'o-', label="Euler")
plt.plot(x_e, y_ec[:, 0], 's-', label="Euler-Cauchy")
plt.plot(x_e, y_rk[:, 0], '^-', label="Runge-Kutta")
plt.plot(x_exact, y_exact_vals, '-', label="Exact")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
