from vectors import *
from scipy import matrix

if __name__ == '__main__':

    print("##### Scaling #####")
    A = matrix([1, 0]).T
    scale = matrix([[1 / 2, 0], [0, 1 / 2]])
    print(scale * A)
    print()

    print("##### Rotation #####")
    A = matrix([1, 0]).T
    rotation = matrix([[0, -1], [1, 0]])
    print(rotation * A)
    print()

    print("##### Reflection #####")
    A = matrix([1, 0]).T
    reflection = matrix([[-1, 0], [0, -1]])
    print(reflection * A)
    print()

    print("##### Vector Plot #####")
    vector = matrix([2, 2]).T
    plot_vector(vector)
    vector_new = rotation * scale * vector
    plot_vector(vector_new)
    print()