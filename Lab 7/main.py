import numpy as np
from scipy.optimize import fsolve


def equations(x, a):
    x1, x2 = x
    f1 = (x1 ** 2 + a ** 2) * x2 - a ** 3
    f2 = (x1 - a / 2) ** 2 + (x2 - a / 2) ** 2 - a ** 2
    return np.array([f1, f2])


def jacobian(x, a):
    x1, x2 = x
    df1_dx1 = 2 * x1 * x2
    df1_dx2 = x1 ** 2 + a ** 2
    df2_dx1 = 2 * (x1 - a / 2)
    df2_dx2 = 2 * (x2 - a / 2)
    return np.array([[df1_dx1, df1_dx2], [df2_dx1, df2_dx2]])


def simple_iteration(x0, a, tol=0.001, maxiter=100):
    x = np.array(x0)
    for i in range(maxiter):
        x_new = np.array([a ** (3 / 2) / (x[1] + a ** 2 * x[0]),
                          np.sqrt(a ** 2 - (x[0] - a / 2) ** 2) + a / 2])
        if np.linalg.norm(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    return x, maxiter


def newton(x0, a, tol=0.001, maxiter=100):
    x = np.array(x0)
    for i in range(maxiter):
        J = jacobian(x, a)
        f = equations(x, a)
        dx = np.linalg.solve(J, -f)
        x_new = x + dx
        if np.linalg.norm(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    return x, maxiter


a = 1.5

x0 = np.array([2.25, 0.5])

# #test
# x_fsolve = fsolve(equations, x0, args=(a,))
# print("Solution using fsolve: ", x_fsolve[0], x_fsolve[1])

x_simple, iter_simple = simple_iteration(x0, a)
print("Solution using simple iteration: ", x_simple[1], x_simple[0], "\nNumber of iterations:", iter_simple)

#x0 = np.array([1, 1])
x_newton, iter_newton = newton(x0, a)
print("Solution using Newton's method: ", x_newton[0], x_newton[1], "\nNumber of iterations:", iter_newton)
