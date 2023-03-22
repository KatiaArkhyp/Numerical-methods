import matplotlib.pyplot as plt

x0 = -1
xK = 1
h1 = 0.5
h2 = 0.25


def function(x):
    y = x / ((3 * x + 7) * (2 * x + 3))
    return y


def rectangle(hRound):
    result = 0
    iterX = x0
    while iterX < xK:
        result += function(iterX + hRound / 2) * hRound
        iterX += hRound
    return result


def trapezoid(hRound):
    X = []
    Y = []
    result = 0
    x = x0
    while x <= xK:
        X.append(x)
        Y.append(function(x))
        x += hRound
    i = 1
    while i < len(X) - 1:
        result += Y[i]
        i += 1
    result *= 2
    result += Y[0]
    result += Y[len(X) - 1]
    result *= hRound / 2

    return result


def simpson(hRound):
    X = []
    Y = []
    result = 0
    x = x0
    while round(x, 3) <= xK:
        X.append(x)
        Y.append(function(x))
        x += hRound
    i = 1
    while i < len(X) - 1:
        result += (Y[i] * 4)
        i += 2
    i = 2
    while i < len(X) - 1:
        result += (Y[i] * 2)
        i += 2
    result += Y[0]
    result += Y[len(X) - 1]
    result *= hRound / 3
    return result


def runge(h, h2, p):
    result = h2 - (h2 - h) / (2 ** p - 1)
    return result


def func_plot():
    xF = []
    yF = []
    x = x0
    while x <= xK:
        xF.append(x)
        yF.append(function(x))
        x += 0.05

    plt.plot(xF, yF, linewidth=2)
    plt.xlabel("X", fontsize=14)
    plt.ylabel("Y", fontsize=14)
    plt.grid()
    plt.show()


print(f"Rectangle method result with step {h1} is {rectangle(h1)}")
print(f"Rectangle method result with step {h2} is {rectangle(h2)}")
print(f"Runge checking result is {runge(rectangle(h1), rectangle(h2), 1)}")
print("--------------------------------------------------------------")
print(f"Trapezoid method result with step {h1} is {trapezoid(h1)}")
print(f"Trapezoid method result with step {h2} is {trapezoid(h2)}")
print(f"Runge checking result is {runge(trapezoid(h1), trapezoid(h2), 2)}")
print("--------------------------------------------------------------")
print(f"Simpson method result with step {h1} is {simpson(h1)}")
print(f"Simpson method result with step {h2} is {simpson(h2)}")
print(f"Runge checking result is {runge(simpson(h1), simpson(h2), 4)}")
func_plot()
