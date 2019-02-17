from plotings import *
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    print('### Practice 1. Scaling 알고리즘 구현 ###')
    # scaling_method_compare_plot()
    # scaling_function_compare_plot()
    print()

    print('### Practice 2. 적합한 데이터 전처리 방법 찾기 ###')
    data = datasets.load_boston()
    dfX = pd.DataFrame(data.data, columns=data.feature_names)
    dfX = dfX.drop(['CHAS', 'RAD'], axis=1)    # 범주형이라 제거
    dfY = pd.DataFrame(data.target, columns=['MEDV'])
    regr = LinearRegression()

    ########################################################
    ###  Data Preprocessing
    dfX.TAX = np.log(dfX.TAX)
    dfX.LSTAT = np.log(dfX.LSTAT)
    ########################################################

    # 분포 확인
    fig, axes = plt.subplots(nrows=11, ncols=1, figsize=(5, 26))
    for i, ax in enumerate(axes):
        sns.kdeplot(dfX.iloc[:, i], ax=ax)
    plt.subplots_adjust(hspace=0.5)
    plt.show()

    n = 1000
    avg = 0
    for i in range(n):
        X_train, X_test, y_train, y_test = train_test_split(dfX, dfY, train_size=0.7, test_size=0.3)
        regr.fit(X_train, y_train)
        avg += regr.score(X_test, y_test)
    print(avg / n)