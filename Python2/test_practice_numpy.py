import numpy as np

print("##### 1. Create an array of size 10 filled with 0 #####")
n1 = np.zeros(10)
print(n1)
print()

print("##### 2. Set fifth value to 1 from above array #####")
n1[4] = 1
print(n1)
print()

print("##### 3. Create an array with values ranging from 10 to 49 #####")
n3 = np.arange(10, 50)
print(n3)
print()

print("##### 4. Create a 5 * 5 matrix with values ranging from 0 to 24 #####")
n4 = np.arange(25).reshape(5, 5)
print(n4)
print()

print("##### 5. Create a 5 * 5 identity matrix #####")
n5 = np.eye(5)
print(n5)
print()

print("##### 6. Create an 5 * 5 array with random values and find the minimum and maximum value #####")
n6 = np.random.random((5, 5))
print(n6)
print("minimum value: {}".format(np.min(n6)))
print("maximum value: {}".format(np.max(n6)))
print()

print("##### 7. Multiply a 4 * 3 matrix by a 3 * 2 matrix #####")
n7a = np.ones((4, 3))
n7b = np.random.random((3, 2))
print(n7a)
print(n7b)
n7c = np.dot(n7a, n7b)
print(n7c)
print()

print("##### 8. Transpose the above matrix #####")
n8 = n7c.transpose()
print(n8)
print()

print("##### 9. Create two matrices ranging from 0 to 24 and 25 to 49. then add and subtract two matrix #####")
n9a = np.arange(25).reshape(5, 5)
n9b = np.arange(25, 50).reshape(5, 5)
n9c = n9a + n9b
n9d = n9a - n9b
print(n9a)
print(n9b)
print(n9c)
print(n9d)
print()