from linearequations import *
import numpy as np
import sympy

if __name__ == '__main__':

    print("##### Solve Ax = b by using A = LU #####")
    print(plusol(np.array([[2, 1, 1], [4, -6, 0], [-2, 7, 2]]), np.array([5, -2, 9])))
    print()

    print("##### Determinant #####")
    print(determ([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(determ([[2, 1, 1], [4, -6, 0], [-2, 7, 2]]))
    print()

    print("##### Matrix Multiplication #####")
    mat1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    mat2 = np.array([[1, 2], [4, 5], [7, 8]])
    print(np.dot(mat1, mat2))
    print(matrixmul(mat1, mat2))
    print()

    print("##### Reduced Row Echelon Form #####")
    A = np.array([[1, 3, 3, 2], [0, 1, 3, 1], [0, 1, 3, 0]])
    print(RREF(A))
    print(sympy.Matrix(A).rref())
    B = np.array([[2, 1, 1], [4, -6, 0], [-2, 7, 2]])
    print(RREF(B))
    print(sympy.Matrix(B).rref())
    print()

    print("##### Paricular solution of Ax=b #####")
    print(paritalSol(np.array([[2, 1, 1], [4, -6, 0], [-2, 7, 2]]), np.array([[5, -2, 9]])))
    print()