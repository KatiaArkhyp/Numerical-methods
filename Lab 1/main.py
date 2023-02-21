import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 10 ** x - 6 * x - 2


def diagram():
    y = lambda x: 10 ** x
    y1 = lambda x: 6 * x + 2
    x = np.linspace(-1, 1)
    plt.plot(x, y(x))
    plt.plot(x, y1(x))
    plt.show()


def halfDivision(a, b, e):
    c = 0
    while b - a > e:
        c = (a + b) / 2
        if f(b) * f(c) < 0:
            a = c
        else:
            b = c
    return c


def chord(a, b, e):
    x = lambda a, b: a - (f(a) * (b - a)) / (f(b) - f(a))
    while math.fabs(f(x(a, b))) > e:
        if f(a) * f(x(a, b)) <= 0:
            b = x(a, b)
        else:
            a = x(a, b)
    return x(a, b)


def newton(x, e):
    while (math.fabs(f(x))) > e:
        x = x - (f(x)) / (math.log(10) * math.pow(10, x) - 6)
    return x


def g1(x):
    return (10 ** x - 2) / 6


def simpleIteration1(a, b, e):
    c = (a + b) / 2
    x = g1(c)
    while (math.fabs(x - c)) >= e:
        c = x
        x = g1(c)
    return x


def g2(x):
    return math.log(6 * x + 2, 10)


def simpleIteration2(a, b, e):
    x = (a + b) / 2
    result = x
    x = g2(x)
    while (math.fabs(x - result)) >= e:
        result = x
        x = g2(x)
    return x


diagram()

print("Метод половинного ділення:")
print(halfDivision(-0.3, 0.2, 0.01))
print(halfDivision(0.7, 0.8, 0.01))
print()

print("Метод Хорд:")
print(chord(-0.3, 0.2, 0.01))
print(chord(0.7, 0.8, 0.01))
print()

print("Метод Ньютона:")
print(newton(-0.3, 0.01))
print(newton(0.7, 0.01))
print()

print("Метод простої ітерації:")
print(simpleIteration1(-0.3, 0.2, 0.01))
print(simpleIteration2(0.7, 0.8, 0.01))
print()
