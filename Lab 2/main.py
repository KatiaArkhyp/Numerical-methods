import math
import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def lagranz():
    Xi = [0, math.pi/6, math.pi/3, math.pi/2]
    Yi = []
    for i in Xi:
        Yi.append(i * np.sin(i))

    print("X:", Xi)
    print("Y:", Yi)

    print("L(x) = " + str(lagranz_Function(var('x'), Xi)))
    print("L(π/4) = " + str(lagranz_Function(math.pi/4, Xi)))

    def absolut_fault():
        xDot = math.pi / 4
        yDot = xDot * np.sin(xDot)

        print("Абсолютна похибка " + str(abs(yDot - lagranz_Function(xDot, Xi))))

    absolut_fault()

def newton():
    Xi = [0, math.pi/6, 5*math.pi/12, math.pi/2]
    Yi = []
    for i in Xi:
        Yi.append(i * np.sin(i))

    print("X:", Xi)
    print("Y:", Yi)

    print("N(x) = " + str(newton_Function(var('x'), Xi)))
    print("N(π/4) = " + str(newton_Function(math.pi/4, Xi)))
    def absolut_fault():
        xDot = math.pi/4
        yDot = xDot * np.sin(xDot)

        print("Абсолютна похибка " + str(abs(yDot - newton_Function(xDot, Xi))))

    absolut_fault()


def lagranz_Function(x, Xi):
    Yi = []

    for i in Xi:
        Yi.append(i * np.sin(i))
    lagr = 0
    i = 0
    while i <= 3:
        if (i == 0):
            lagr += Yi[i] * (((x - Xi[1])*(x - Xi[2])*(x - Xi[3]))/((Xi[0] - Xi[1])*(Xi[0] - Xi[2])*(Xi[0] - Xi[3])))
        elif(i == 1):
            lagr += Yi[i] * (((x - Xi[0])*(x - Xi[2])*(x - Xi[3]))/((Xi[1] - Xi[0])*(Xi[1] - Xi[2])*(Xi[1] - Xi[3])))
        elif(i == 2):
            lagr += Yi[i] * (((x - Xi[0])*(x - Xi[1])*(x - Xi[3]))/((Xi[2] - Xi[0])*(Xi[2] - Xi[1])*(Xi[2] - Xi[3])))
        else:
            lagr += Yi[i] * (((x - Xi[0])*(x - Xi[1])*(x - Xi[2]))/((Xi[i] - Xi[0])*(Xi[i] - Xi[1])*(Xi[i] - Xi[2])))
        i += 1
    return lagr

def newton_Function(x, Xi):
    Yi = []
    for i in Xi:
        Yi.append(i * np.sin(i))

    newtn = 0

    i = 0
    while i <= 3:
        if (i == 0):
            newtn += Yi[0]
        elif (i == 1):
            newtn += ((Yi[1] - Yi[0])/(Xi[1] - Xi[0]))*(x - Xi[0])
        elif (i == 2):
            newtn += ((((Yi[2] - Yi[1])/(Xi[2] - Xi[1])) - ((Yi[1] - Yi[0])/(Xi[1
                ] - Xi[0])))/(Xi[2] - Xi[0]))*(x - Xi[0])*(x - Xi[1])
        else:
            newtn += ((((((Yi[3] - Yi[2])/(Xi[3] - Xi[2])) - ((Yi[2] - Yi[1])/(Xi[2
            ] - Xi[1])))/(Xi[3] - Xi[1])) - ((((Yi[2] - Yi[1
            ]) / (Xi[2] - Xi[1])) - ((Yi[1] - Yi[0]) / (Xi[1] - Xi[0]))) / (Xi[2] - Xi[0])))/(Xi[3
            ] - Xi[0]))*(x - Xi[0])*(x - Xi[1])*(x - Xi[2])
        i += 1
    return newtn


def graphLagranz():
    X1 = [0, math.pi / 6, math.pi / 3, math.pi / 2]
    X2 = [0, math.pi/6, 5*math.pi/12, math.pi/2]
    y = lambda x: lagranz_Function(x, X1)
    y1 = lambda x: lagranz_Function(x, X2)
    fig = plt.subplots()
    x = np.linspace(-5, 10, 200)
    plt.plot(x, y(x), label="Lagranz func for first diapason")
    plt.plot(x, y1(x), label="Lagranz func for second diapason")
    plt.legend()
    plt.show()

def graphNewton():
    X1 = [0, math.pi / 6, math.pi / 3, math.pi / 2]
    X2 = [0, math.pi/6, 5*math.pi/12, math.pi/2]
    y = lambda x: newton_Function(x, X1)
    y1 = lambda x: newton_Function(x, X2)
    fig = plt.subplots()
    x = np.linspace(-5, 10, 200)
    plt.plot(x, y(x), label="Newton func for first diapason")
    plt.plot(x, y1(x), label="Newton func for second diapason")
    plt.legend()
    plt.show()



graphLagranz()
graphNewton()
print("\x1B[4m" + "\nМетод Лагранжа" + "\x1B[0m")
lagranz()
print("\x1B[4m" + "\nМетод Ньютона" + "\x1B[0m")
newton()
