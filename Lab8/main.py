import numpy as np

a = 0.1
b = 1.1
h = 0.2
n = int((b - a) / h) + 1

x = np.linspace(a, b, n)
A = np.zeros(n - 2)
B = np.zeros(n - 2)
C = np.zeros(n - 2)
D = np.zeros(n - 2)
E = np.zeros(n - 2)

for i in range(1, n - 1):
    A[i - 1] = 1 / h ** 2 - np.exp(x[i]) / (2 * h)
    B[i - 1] = -2 / h ** 2 - 1
    C[i - 1] = 1 / h ** 2 + np.exp(x[i]) / (2 * h)
    D[i - 1] = -2 - h * np.exp(x[i])
    E[i - 1] = -2 + h ** 2 * 2

alpha = np.zeros(n - 1)
beta = np.zeros(n - 1)

alpha[1] = A[0] / B[0]
beta[1] = D[0] / B[0]

for i in range(1, n - 2):
    alpha[i + 1] = A[i] / (B[i] - C[i] * alpha[i])
    beta[i + 1] = (D[i] + C[i] * beta[i]) / (B[i] - C[i] * alpha[i])

y = np.zeros(n)

y[0] = 1
y[n - 1] = -y[n - 2]

for i in range(n - 3, -1, -1):
    y[i + 1] = alpha[i + 1] * y[i + 2] + beta[i + 1]
dy = np.zeros(n)

for i in range(1, n - 1):
    dy[i] = (y[i + 1] - y[i - 1]) / (2 * h)

dy[0] = 1  # задано початкову умову y'(0.1) = 1
dy[n - 1] = -y[n - 2] - y[n - 1]  # задано крайову умову y(1.1) + y'(1.1) = 0
d2y = np.zeros(n)

for i in range(1, n - 1):
    d2y[i] = (y[i + 1] - 2 * y[i] + y[i - 1]) / h ** 2 - np.exp(x[i]) * dy[i]

d2y[0] = 1  # y'(0.1) = 1
d2y[n - 1] = -d2y[n - 2] - np.exp(x[n - 1]) * dy[n - 1] - 2  # y(1.1) + y'(1.1) = 0

# for i in range(n):
#     print("x =", round(x[i], 1), "y =", round(y[i], 5), "y' =", round(dy[i], 5), "y'' =", round(d2y[i], 5))

print("{:<8} {:<8} {:<8} {:<8}".format("x", "y", "y\'", "y\'\'"))
print("-" * 35)
for i in range(n):
    print("{:<8.1f} {:<8.5f} {:<8.5f} {:<8.5f}".format(x[i], y[i], dy[i], d2y[i]))
