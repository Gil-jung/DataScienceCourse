import numpy as np
from scipy import stats
from scipy import linalg
import matplotlib.pyplot as plt
from scipy import optimize

print("##### 1-(a). 정규분포를 따르는 random sample 500개 생성 #####")
samples = np.random.normal(size=500)
print()
print("##### 1-(b). 위 sample 의 중앙값 #####")
print(np.median(samples))
print()
print("##### 1-(c). 위 sample 의 표준편차 #####")
print(np.std(samples))
print()
print("##### 1-(d). 위 sample 의 상위 20% 값 #####")
print(stats.scoreatpercentile(samples, 80))
print()
print("##### 1-(e). 위 sample 의 정규분포 추측 후 평균과 표준편차 #####")
loc, std = stats.norm.fit(samples)
print("평균: %s, 표준편차: %s" % (loc, std))
print()
print()
print("##### 2-(a). 주어진 행렬의 determinant #####")
arr = np.array([[1, 3, 5], [2, 4, 6], [6, 5, 8]])
print(linalg.det(arr))
print()
print("##### 2-(b). 주어진 행렬의 역행렬 #####")
print(linalg.inv(arr))
print()
print()
print("##### 3. 주어진 행렬의 determinant 구할때 오류발생 원인 #####")
arr2 = np.array([[1, 2, 3, 4], [3, 8, 5, 2], [4, 3, 6, 2]])
print("square matrix 가 아니므로 value error 발생")
print()
print()
print("##### 5. Scipy 사용하여 LU 분해 #####")
A = np.array([[2, 2, 2], [4, 7, 7], [6, 18, 22]])
P, L, U = linalg.lu(A)
print('P = \n' + str(P))
print('L = \n' + str(L))
print('U = \n' + str(U))
print('A = PLU = \n' + str(np.dot(P, L).dot(U)))
print()
print()
print("##### 6. 진폭이 4, 주기가 2인 cos 형태의 파동을 만들고, 정규분포를 따르는 noise 추가 #####")
np.random.seed(0)
x_data = np.linspace(-5, 5, num=50)
y_data = 4 * np.cos(2 * x_data) + np.random.normal(size=50)
plt.scatter(x_data, y_data)
plt.show()
print()
print()
print("##### 7. 6번 문제의 파동 Data가 cos 함수 및 sin 함수로 생성됬을때 진폭과 주기 #####")
def cos_func(x, a, b):
    return a * np.cos(b * x)
def sin_func(x, a, b):
    return a * np.sin(b * x)
params_cos, params_covariance_cos = optimize.curve_fit(cos_func, x_data, y_data, p0=[2, 2])
params_sin, params_covariance_sin = optimize.curve_fit(sin_func, x_data, y_data, p0=[2, 2])
print("cos 함수(진폭, 주기): %s " % params_cos)
print("sin 함수(진폭, 주기): %s " % params_sin)
print()
print()
print("##### 8. 두 반의 몸무게 분포의 기댓값이 동일한지 검정 #####")
class1 = [65.9, 53.6, 57.3, 59.3, 63.8, 59.2, 64.2, 75.0, 62.9]
class2 = [76.3, 82.1, 73.3, 69.3, 59.9, 72.1, 59.1, 86.8, 78.1]
result = stats.ttest_ind(class1, class2)
print("독립표본 t 검정 결과 : %.4f, pvalue=%.3f" %(result))
print()