import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

x = np.array([0.1, 0.5, 0.9, 1.3, 1.7])
f = np.array([100.0, 4.0, 1.2346, 0.59172, 0.34602])

cs = CubicSpline(x, f, bc_type='natural')

x_star = 8
print(f'f({x_star}) = {cs(x_star)}')

xx = np.linspace(0.1, 1.7, 1000)
yy_cub = cs(xx)
plt.plot(xx, yy_cub, label='Cubic Spline')
plt.plot(x, f, 'o', label='Data points')
plt.legend()
plt.show()
