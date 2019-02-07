# from scipy.stats import binom
#
# # 어느 제품의 불량율은 10% 이다. 임의의 5개의 제품 중에 불량품이 3개일 확률은?
# print(round(binom.pmf(3, 5, 0.1), 3))
#
# # 어느 제품의 불량율은 10%이다. 임의의 20개의 제품 중에 불량품이 5개 이하일 확률은?
# print(round(binom.cdf(5, 20, 0.1), 3))
#
# # 불량품이 4개 이상일 확률은?
# print(round(1 - binom.cdf(3, 20, 0.1), 3))
# print()
#
# # binom.ppf(q, n, p): 이항분포의 백분위수,  q: 구하고 싶은 분위수
# print(binom.ppf(q=0.1875, n=5, p=0.5))
#
# # binom.rvs(n, p, size): 난수생성, size: 난수의 개수
# print(binom.rvs(5, 0.5, size=3))
#
# # 이항분포 확률분포함수 그리기
# x = range(7)
# fx = binom.pmf(x, 6, 0.5)
#
# import matplotlib.pyplot as plt
#
# def binom_plot():
#     plt.plot(x, fx, marker='o', linestyle='')
#     plt.vlines(x, 0, fx)
#     plt.show()
#
# binom_plot()


# 균일분포
# from scipy.stats import uniform
#
# # x: 균일 분포를 따르는 확률변수값
# # loc: 균일 분포에서 하한값(a)
# # scale: 균일 분포에서 상한값(b)
# # q: 구하고 싶은 분위수
# print(uniform.pdf(x=1, loc=0, scale=2))
# print(uniform.cdf(x=1, loc=0, scale=2))
# print(uniform.ppf(q=0.5, loc=0, scale=2))
# print(uniform.rvs(loc=0, scale=2, size=2))


# 정규분포
# from scipy.stats import norm
#
# print(round(norm.pdf(x=0, loc=0, scale=1), 3))
#
# # 정규분포의 확률밀도함수 그리기
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(-5, 5.1, 0.1)
# fx = norm.pdf(x=x, loc=0, scale=1)
#
# def norm_plot():
#     plt.plot(x, fx)
#     plt.xlabel("x")
#     plt.ylabel("fx")
#     plt.title("pdf of standard normal dist")
#     plt.show()
#
# norm_plot()

# # 전구의 수명이 평균이 2000, 표준편차가 200인 정규분포를 따를 때, 전구의 수명이 2500시간 이하일 확률은?
# print(round(norm.cdf(x=2500, loc=2000, scale=200), 3))
#
# # 전구의 수명이 1800시간 이상일 확률은?
# print(round(1 - norm.cdf(x=1800, loc=2000, scale=200), 3))
#
# # 어느 시험에서 상위 2%이내의 점수를 받아야 합격이라고 한다.
# # 만약 시험의 점수가 평균이 100, 표준편차가 15인 정규분포를 따를 때,
# # 시험에 합격하기 위해서는 약 몇 점 이상의 점수를 받아야 하는가?
# print(round(norm.ppf(q=0.98, loc=100, scale=15), 3))
# print()
#
# print(norm.rvs(loc=5, scale=10, size=5))


## 이항분포의 정규근사 그래프 그리기

# import matplotlib.pyplot as plt
# from scipy.stats import binom, norm
# def binom_to_norm():
#     plt.subplot(131)
#     plt.xlim(-3, 15)
#     plt.plot(range(11), binom.pmf(range(11), n=10, p=0.1), marker='o')
#     plt.plot(range(-3, 15), norm.pdf(range(-3, 15), loc=1, scale=np.sqrt(0.9)), color='black')
#     plt.subplot(132)
#     plt.xlim(-3, 15)
#     plt.plot(range(16), binom.pmf(range(16), n=30, p=0.1), marker='o')
#     plt.plot(range(-3, 15), norm.pdf(range(-3, 15), loc=3, scale=np.sqrt(2.7)), color='black')
#     plt.subplot(133)
#     plt.xlim(-3, 15)
#     plt.plot(range(26), binom.pmf(range(26), n=50, p=0.1), marker='o')
#     plt.plot(range(-3, 15), norm.pdf(range(-3, 15), loc=5, scale=np.sqrt(4.5)), color='black')
#     plt.show()
#
# binom_to_norm()

# ## 카이제곱분포의 pdf 그리기
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import chi2
#
# x = np.arange(0, 40.1, 0.1)
# def chi2_plot():
#     plt.plot(x, chi2.pdf(x, 3), color='black', label='df 3')
#     plt.plot(x, chi2.pdf(x, 6), color='rosybrown', label='df 6')
#     plt.plot(x, chi2.pdf(x, 9), color='seagreen', label='df 9')
#     plt.plot(x, chi2.pdf(x, 20), color='blueviolet', label='df 20')
#
#     plt.legend(loc='upper right')
#     plt.show()
#
# chi2_plot()
#
# ## t분포의 pdf 그리기
# from scipy.stats import t, norm
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(-5, 5.1, 0.1)
# def t_plot():
#     plt.plot(x, t.pdf(x, 3), color='black', label='df 3')
#     plt.plot(x, t.pdf(x, 6), color='rosybrown', label='df 6')
#     plt.plot(x, t.pdf(x, 9), color='seagreen', label='df 9')
#     plt.plot(x, t.pdf(x, 20), color='blueviolet', label='df 20')
#     plt.plot(x, norm.pdf(x, 0, 1), color='tomato', label='normal')
#
#     plt.legend(loc='upper right')
#     plt.show()
#
# t_plot()
#
## F분포의 pdf 그리기
# from scipy.stats import f
# import matplotlib.pyplot as plt
# import numpy as np
#
# def f_plot():
#     x = np.arange(0.001, 4.1, 0.1)
#
#     plt.subplot(131)
#     plt.plot(x, f.pdf(x, 3, 20), color='seagreen', label='k2=20')
#     plt.plot(x, f.pdf(x, 3, 10), color='blueviolet', label='k2=10')
#     plt.plot(x, f.pdf(x, 3, 6), color='coral', label='k2=6')
#     plt.plot(x, f.pdf(x, 3, 3), color='black', label='k2=3')
#     plt.title('f dist w.r.t. k1=3')
#     plt.legend(loc='upper right')
#
#     plt.subplot(132)
#     plt.plot(x, f.pdf(x, 10, 20), color='seagreen', label='k2=20')
#     plt.plot(x, f.pdf(x, 10, 10), color='blueviolet', label='k2=10')
#     plt.plot(x, f.pdf(x, 10, 6), color='coral', label='k2=6')
#     plt.plot(x, f.pdf(x, 10, 3), color='black', label='k2=3')
#     plt.title('f dist w.r.t. k1=10')
#     plt.legend(loc='upper right')
#
#     plt.subplot(133)
#     plt.plot(x, f.pdf(x, 20, 20), color='seagreen', label='k2=20')
#     plt.plot(x, f.pdf(x, 20, 10), color='blueviolet', label='k2=10')
#     plt.plot(x, f.pdf(x, 20, 6), color='coral', label='k2=6')
#     plt.plot(x, f.pdf(x, 20, 3), color='black', label='k2=3')
#     plt.title('f dist w.r.t. k1=20')
#     plt.legend(loc='upper right')
#     plt.show()
#
# f_plot()
#
# # (1)
# n = 49; sigma = 30; xbar = 157.02; alpha=0.05; d=5
#
# z_alpha = norm.ppf(1-alpha/2)
#
# c_i = np.array([round(xbar - z_alpha * sigma/np.sqrt(n), 3), round(xbar + z_alpha * sigma/np.sqrt(n), 3) ])
# print(c_i)
#
# # (2)
# min_n = (z_alpha * sigma / d)**2
# print(np.ceil(min_n))
#
# ## n=64, 표본평균=27.75, 표본표준편차-5.083 인 표본을 토대로 모평균의 99% 신뢰구간을 추정해보도록 하자
# n = 64; sigma = 5.083; xbar = 27.75; alpha = 0.01
#
# t_alpha = t.ppf(1 - alpha/2, n-1)
# print(round(t_alpha, 3))
#
# c_i = np.array([round(xbar - t_alpha * sigma/np.sqrt(n), 3), round(xbar + t_alpha * sigma/np.sqrt(n), 3)])
# print(c_i)
#
# bulb = np.array([2000, 1975, 1900, 2000, 1950, 1850, 1950, 2100, 1975])
# import scipy.stats as st
#
# tt = st.ttest_1samp(bulb, 1950)
# # ttest_1samp: 일표본 t검정 함수
# print(round(tt.statistic, 3))
# # ttest_1samp를 이용한 검정통계량
#
# m = np.mean(bulb)
# #표본평균
#
# s = np.std(bulb) * np.sqrt(9/8)
# # 표본표준편차 - numpy에서 지원하는 분산 및 표준편차는 모분산과 모표준편차의 값을 제공한다. 표본분산과 표본표준편차의
# # 값을 얻기 위해서는 각각 n/n-1, sqrt(n/n-1)을 곱해주어야 한다.
#
# print(round((m - 1950)/(s/np.sqrt(9)), 3))
# # 식을 이용해 직접 계산한 검정통계량. 둘의 값은 같다.
#
# print(round(tt.pvalue/2, 3))
# ## ttest_1samp를 이용한 유의확률
#
# print(round(1-t.cdf(tt.statistic, 8), 3))
#
# sc_xbar = 0.62; sc_s = 0.11;
#
# t_0 = (sc_xbar-0.6) / (sc_s/np.sqrt(120))
# print(round(t_0, 3))
# # 검정통계량의 관측값
#
# print(round(t.ppf(0.975, 119), 3))
# # 기각역의 경계값
# print(round(norm.ppf(0.975), 3))
# # 정규근사 확인
# # 검정통계량이 기각역에 포함되므로 귀무가설을 기각할 수 있다.
#
# print(round(2*(1-t.cdf(t_0, 119)),3))
# # 유의확률
#
# n = 6; sigma_d = 0.443; dbar = 0.2; alpha=0.05
# print(np.array([round(dbar - t.ppf(1-alpha/2, n-1)*sigma_d/np.sqrt(n), 3), round(dbar + t.ppf(1-alpha/2, n-1)*sigma_d/np.sqrt(n),3)]))
#
# cow_1 = np.array([24.7, 46.1, 18.5, 29.5, 26.3, 33.9, 23.1, 20.7, 18.0, 19.3, 23.0])
# cow_2 = np.array([12.4, 14.1, 7.6, 9.5, 19.7, 10.6, 9.1, 11.5, 13.3, 8.3, 15.0])
# cow_d = cow_1 - cow_2
#
# print(round(t.ppf(0.99, 10), 3))
# # 기각역의 경계값
#
# cow_tt=st.ttest_rel(cow_1, cow_2)
# # ttest_rel : 대응비교 t검정 함수
# print(round(cow_tt.statistic, 3))
# # ttest_rel을 사용한 검정통계량
#
# d = np.mean(cow_d)
# # 차이의 평균
# s = np.std(cow_d)*np.sqrt(11/10)
# # 차이의 표준편차
#
# print(round(d/(s/np.sqrt(11)), 3))
# # 식을 이용하여 계산한 검정통계량, 둘의 결과는 같다.
#
# print(round(cow_tt.pvalue/2, 4))
# # 유의확률
# # 검정통계량이 기각역에 포함되고, 유의확률이 0.1보다 작으므로 귀무가설을 기각할 수 있따.
#
# x_1 = np.array([19.54, 14.47, 16.00, 24.83, 26.39, 11.49])
# x_2 = np.array([15.95, 25.89, 20.53, 15.52, 14.18, 16.00])
#
# S_p = np.sqrt(((6)*np.var(x_1)+(6)*np.var(x_2))/(6+6-2))
# # Pooled standard deviation
#
# tt = st.ttest_ind(x_1, x_2, equal_var=True)
# # 등분산 가정
# # ttest_ind : 독립이표본 t검정 함수
#
# print(round(tt.statistic, 3))
# # 검정통계량
#
# print(round(tt.pvalue, 3))
# # 유의확률
# # 귀무가설을 기각할 수 없다.
#
# x_1 = np.array([12.7, 19.3, 20.5, 10.5, 14.0, 10.8, 16.6, 14.0, 17.2])
# x_2 = np.array([18.2, 32.9, 10.0, 14.3, 16.2, 27.6, 15.7])
#
# tt = st.ttest_ind(x_1, x_2, equal_var=False)
# print(round(tt.statistic, 3))
# # 검정통게량
#
# print(round(tt.pvalue/2, 3))
# # 유의확률
# # 귀무가설을 기각할 수 없다.
#
# from scipy.stats import chi2
#
# x = np.array([226, 228, 226, 225, 232, 228, 227, 229, 225, 230])
# sdx = np.std(x)*np.sqrt(10/9)
# chisq = (10-1)*(sdx**2)/(1.5**2)
# print(round(chisq, 3))
#
# print(round(chi2.ppf(0.95, 9), 3))
# # 기각역의 경계값
#
# print(round(1-chi2.cdf(chisq,9), 3))
# # 유의확률
# # 귀무가설을 기각할 수 있다.
#
# print(np.array([round(chisq*(1.5**2)/(chi2.ppf(0.95, 9)), 3), round(chisq*(1.5**2)/(chi2.ppf(0.05, 9)), 3)]))


######### 실습 예제 ###########
# 모든 검정은 유의수준 5%로 통일한다.

# 1. 실제모수 mu = 0.5인 베르누이 확률 변수의 시뮬레이션을 통해 평균이 0,5인지 검정해보아라.(난수 개수는 100)

from scipy.stats import bernoulli
import numpy as np
import scipy.stats as st
from scipy.stats import t

np.random.seed(0)
x = bernoulli.rvs(0.5, size=100)
print(x)

n = np.count_nonzero(x)
print(n)

t1 = st.ttest_1samp(x, 0.5)
print(round(t1.statistic, 3))
print(round((np.mean(x)-0.5)/((np.std(x)*np.sqrt(100/99))/np.sqrt(100)),3))

print(round(t1.pvalue, 3))
print(round(2*(t.cdf(t1.statistic, 99)),3))

# 2. 실제모수 mu = 0.35인 베르누이 확률 변수의 시뮬레이션을 통해 귀무 가설 h0: mu = 0,5인지 검정해보아라.(난수 개수는 100)
y = bernoulli.rvs(0.35, size=100)
print(y)
print(np.count_nonzero(y))

t2 = st.ttest_1samp(y, 0.5)
print(round(t2.statistic, 3))
print(round((np.mean(y)-0.5)/((np.std(y)*np.sqrt(100/99))/np.sqrt(100)),3))

print(round(t2.pvalue, 3))
print(round(2*(t.cdf(t2.statistic, 99)), 3))