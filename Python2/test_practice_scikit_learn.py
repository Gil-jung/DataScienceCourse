from visualizations import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

if __name__ == '__main__':

    print("######### KNN MeshGrid Coloring ##########")
    n_neighbors = 15
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = iris.target
    x_min, x_max, y_min, y_max = 3.3, 8.9, 1.0, 5.4
    h = .02
    clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, weights='uniform')
    clf.fit(X, y)
    print(clf)

    meshgrid_coloring(x_min, x_max, y_min, y_max, h, X, y, clf, n_neighbors)

