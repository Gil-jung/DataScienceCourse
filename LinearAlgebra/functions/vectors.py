from scipy import matrix
import matplotlib.pyplot as plt

def plot_vector(vector):
    origin = matrix([0, 0]).T
    plt.figure(figsize=(5, 5))
    plt.quiver(*origin, *vector, angles='xy', scale_units='xy', scale=1)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.show()