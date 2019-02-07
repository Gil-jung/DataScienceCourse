from linearequations import *

if __name__ == '__main__':

    print("##### Solve Ax = b by using A = LU #####")
    print(plusol(np.array([[2, 1, 1], [4, -6, 0], [-2, 7, 2]]), [5, -2, 9]))
    print()

    print("##### Determinant #####")
    print(determ([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print()

    print("##### Matrix Multiplication #####")
    mat1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    mat2 = np.array([[1, 2], [4, 5], [7, 8]])
    print(np.dot(mat1, mat2))
    print(matrixmul(mat1, mat2))
    print()