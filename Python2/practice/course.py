### Linear Regression Concept

# from random import *
# import numpy as np
# from sklearn import linear_model
# import matplotlib.pyplot as plt
#
# length = 10
# x = np.array(range(0, length)).reshape(length, 1)
# y = np.array([random()*10 for i in range(length)]).reshape(length, 1)
# print("x: Numpy (10x1) 2D Array: ", "\n", "array(", "\n", x, ")")
# print("y: Numpy (10x1) 2D Array: ", "\n", "array(", "\n", y, ")")
#
# regr = linear_model.LinearRegression()
# regr.fit(x, y)
#
# plt.scatter(x, y, color="black")
# plt.plot(x, regr.predict(x), color='blue', linewidth=3)
# plt.show()

### Linear Regression Example ###
#
# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn import datasets, linear_model
#
# diabetes = datasets.load_diabetes()
# diabetes_X = diabetes.data[:, np.newaxis, 2]
# # print(diabetes_X)
#
# diabetes_X_train = diabetes_X[:-20]
# diabetes_X_test = diabetes_X[-20:]
# diabetes_y_train = diabetes.target[:-20]
# diabetes_y_test = diabetes.target[-20:]
#
# # Create Linear regression object
# regr = linear_model.LinearRegression(copy_X=0)
#
# # Train the model using the training sets
# regr.fit(diabetes_X_train, diabetes_y_train)
# print(regr)
#
# # The coefficients
# print('Coefficients: \n', regr.coef_)
#
# # The intercept
# print("Intercept: \n", regr.intercept_)
#
# # The mean squared error
# print('Mean squared error: %.2f' %
#       np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
#
# # Explained variance score: 1 is perfect prediction
# print('Variance score : %.2f' %
#       regr.score(diabetes_X_test, diabetes_y_test))
#
# # Plot outputs
# plt.scatter(diabetes_X_test, diabetes_y_test, color = 'black')
# plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color = 'blue')
# plt.xticks(())
# plt.yticks(())
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from sklearn import neighbors, datasets
#
# n_neighbors = 15
#
# iris = datasets.load_iris()
# X = iris.data[:, :2]
# y = iris.target
# h = .02
#
# cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
# plt.scatter(X[:,0], X[:, 1], c=y)
# plt.show()
#
# # we create an instance of Neighbors Classifier and fit the data.
# clf = neighbors.KNeighborsClassifier(n_neighbors, weights='uniform')
# clf.fit(X, y)
# print(clf)
#
# new_comer = np.array([[3.7, 4.5]])
# iris_class = clf.predict(new_comer)
# print("The iris class for new point: ", iris_class)


from random import *
import numpy as np
from sklearn import linear_model, tree

length = 10
x = []
y = []
for i in range(length):
    x.append(i)
    y.append(round(random()*10, 2))

print("x: Python (10x1) 1D Array: ", "\n", x)
print()
print("y: Python (10x1) 1D Array: ", "\n", y)
print()
xy_data = []
for i in range(length):
    xy_data.append([x[i], y[i]])

print("xy_data: : Python (10x2) 2D Array ", "\n", xy_data)
print()
z_data = [[1], [1], [1], [1], [1], [2], [2], [2], [2], [2]]
print("z_data: : Python (10x1) 2D Array ", "\n", z_data)
print()

clf = tree.DecisionTreeClassifier()
clf.fit(xy_data, z_data)

print(clf.predict([[3, 3.01]]))
print(clf.predict( np.array([[7, 8.01]])))