import numpy as np


def gauss_jordan_method():
    A = np.array([[1, 2, -1, -7],
                  [8, 0, -9, -3],
                  [2, -3, 7, 1],
                  [1, -5, -6, 8]], dtype=float)

    B = np.array([-23, 39, -7, 30], dtype=float)

    A_B = np.column_stack((A, B))
    print("Matrix A|B:\n", A_B, "\n")

    A = np.vstack([A, np.zeros(4)])
    B = np.append(B, 0)

    for i in range(4):
        pivot = A[i, i]
        A[i] = A[i] / pivot
        B[i] = B[i] / pivot
        for j in range(i + 1, 4):
            factor = A[j, i]
            A[j] = A[j] - factor * A[i]
            B[j] = B[j] - factor * B[i]

    for i in range(3, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = A[j, i]
            A[j] = A[j] - factor * A[i]
            B[j] = B[j] - factor * B[i]

    for i in range(4):
        pivot = A[i, i]
        for j in range(4):
            if i != j:
                factor = A[j, i]
                A[j] = A[j] - factor * A[i]
                B[j] = B[j] - factor * B[i]
        A[i] = A[i] / pivot
        B[i] = B[i] / pivot

    print("Results with Gauss-Jordan method: ")
    for k in range(4):
        print(f"x{k + 1} = {B[k]:.2f}")

    M = np.column_stack((A, B))
    print("\nResult matrix:\n", M)


def seidel_method():
    A = np.array([[14, -4, -2, 3],
                  [-3, 23, -6, -9],
                  [-7, -8, 21, -5],
                  [-2, -2, 8, 18]], dtype=float)
    B = np.array([38, -195, -27, 142], dtype=float)
    n = len(B)

    A_B = np.column_stack((A, B))
    print("Matrix A|B:\n", A_B, "\n")
    x0 = np.zeros(n)

    max_iter = 100
    tolerance = 0.001

    for i in range(max_iter):
        x1 = np.copy(x0)
        for j in range(n):
            x1[j] = (B[j] - np.dot(A[j, :j], x1[:j]) - np.dot(A[j, j + 1:], x0[j + 1:])) / A[j, j]

        if np.linalg.norm(x1 - x0) < tolerance:
            break
        x0 = np.copy(x1)
        print("Iteration", i + 1, x0)

    print("\nResults with Seidel method: ")
    print([f"{x:.2f}" for x in x1])
    print("Number of iterations:", i + 1)


def main():
    print("\033[92mGauss Jordan method\n\033[0m")
    gauss_jordan_method()
    print("-" * 50)
    print("\033[94mSeidel method\n\033[0m")
    seidel_method()


main()
