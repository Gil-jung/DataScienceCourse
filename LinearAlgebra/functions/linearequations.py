from scipy import linalg
import numpy as np


def plusol(A, b):
    P, L, U = linalg.lu(A)
    m, n = np.shape(A)
    y = np.zeros((m, 1))
    c = np.dot(P, b)

    for j in range(m):
        y[j] = c[j] - np.dot(L[j, :j], y[:j])

    x = np.zeros((n, 1))

    for j in range(n - 1, -1, -1):
        x[j] = (y[j] - np.dot(U[j, j + 1:], x[j + 1:])) / U[j, j]

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