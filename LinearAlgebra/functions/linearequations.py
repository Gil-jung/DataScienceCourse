from scipy import linalg
from scipy import matrix
import numpy as np
import matplotlib.pyplot as plt


def plusol(A, b):
    P, L, U = linalg.lu(A)
    m, n = np.shape(A)
    y = np.zeros((m, 1))
    c = np.dot(P, b)

    for j in range(m):
        y[j] = c[j] - np.dot(L[j, :j], y[:j])

    x = np.zeros((n, 1))

    for j in range(n-1, -1, -1):
        x[j] = (y[j] - np.dot(U[j, j+1:], x[j+1:])) / U[j, j]

    return x


def determ(A):
    P, L, U = linalg.lu(A)
    d = linalg.det(P) * np.prod(np.diag(U))
    return d


def matrixmul(mat1, mat2):
    newmat = []
    for i in range(len(mat1)):
        newmati = []
        for k in range(len(mat2[0])):
            newmatik = 0
            for j in range(len(mat2)):
                newmatik += mat1[i][j]*mat2[j][k]
            newmati.append(newmatik)
        newmat.append(newmati)
    return newmat


def RREF(matrix):
    # m : the number of rows
    # n : the number of columns
    m, n = matrix.shape
    A = matrix.astype(float).copy()

    pcol_list = []
    prow = -1
    pcol = -1

    # For each columns
    while True:
        prow += 1
        pcol += 1
        if prow == m or pcol == n: break
        pid = np.argmax(abs(A[prow:,pcol])) + prow

        # Get pivot value
        pivot = float(A[pid, pcol])
        if pivot == 0:
            prow -= 1
            continue
        else:
            pcol_list.append(pcol)
            A[prow, :], A[pid, :] = A[pid, :].copy(), A[prow, :].copy()

            # Substitution each rows
            for i in range(m):
                if prow == i: continue
                mul = float(A[i, pcol]) / pivot
                A[i, :] = A[i, :] - A[prow, :] * mul
            A[prow, :] /= pivot
            A = np.around(A, 4)

    return A, pcol_list


def paritalSol(matrix, b):
    m, n = matrix.shape
    R, pivcol = RREF(np.concatenate((matrix, b.T), axis=1))
    if max(pivcol) == n+1:
        print("No Solution")
        return []
    else:
        r = len(pivcol)
        return R[:, n][0:r]


def plot_vector(vector):
    origin = matrix([0, 0]).T
    plt.figure(figsize=(5, 5))
    plt.quiver(*origin, *vector, angles='xy', scale_units='xy', scale=1)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.show()