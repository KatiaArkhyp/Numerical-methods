import numpy as np
import matplotlib.pyplot as plt

a = 1.5


def f1(x1, x2):
    return (x1 ** 2 + a ** 2) * x2 - a ** 3


def f2(x1, x2):
    return (x1 - a / 2) ** 2 + (x2 - a / 2) ** 2 - a ** 2


x1_vals = np.linspace(-1, 3.5, 100)
x2_vals = np.linspace(-2, 2.5, 100)
x1_grid, x2_grid = np.meshgrid(x1_vals, x2_vals)

f1_vals = f1(x1_grid, x2_grid)
f2_vals = f2(x1_grid, x2_grid)

plt.contour(x1_grid, x2_grid, f1_vals, levels=[0], colors='red')
plt.contour(x1_grid, x2_grid, f2_vals, levels=[0], colors='blue')

plt.xlabel('x1')
plt.ylabel('x2')
plt.grid()
plt.show()



