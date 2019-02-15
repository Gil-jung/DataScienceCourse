import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def meshgrid_coloring(x_min, x_max, y_min, y_max, h, X, y, model, n_neighbors):
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    xr = xx.ravel()
    yr = yy.ravel()
    xy = np.c_[xr, yr]
    Z = model.predict(xy)
    Z = Z.reshape(xx.shape)

    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.title("3-Class classification (k = %i, weights = 'uniform')" % (n_neighbors))
    plt.show()
