import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.DataFrame({   # 정규 분포를 따르는 임의 데이터 생성
    'x1': np.random.normal(0, 2, 1000),
    'x2': np.random.normal(5, 3, 1000),
    'x3': np.random.normal(-5, 5, 1000)
})
df2 = pd.DataFrame({
    # positive skew
    'x1': np.random.chisquare(8, 1000),
    # negative skew
    'x2': np.random.beta(8, 2, 1000) * 40,
    # no skew
    'x3': np.random.normal(50, 3, 1000)
})
df3 = pd.DataFrame({
    # positive skew
    'x1': np.random.chisquare(8, 1000),
    # negative skew
    'x2': np.random.beta(8, 2, 1000) * 40,
    # no skew
    'x3': np.random.normal(50, 3, 1000)
})
df4 = pd.DataFrame({
    # Distribution with lower outliers
    'x1': np.concatenate([np.random.normal(20, 1, 1000), np.random.normal(1, 1, 25)]),
    # Distribution with higher outliers
    'x2': np.concatenate([np.random.normal(30, 1, 1000), np.random.normal(50, 1, 25)])
})

scaler1 = preprocessing.StandardScaler()
scaler2 = preprocessing.MinMaxScaler()
scaler3 = preprocessing.MaxAbsScaler()
scaler4 = preprocessing.RobustScaler()

def scale_standard(lst):
    return (lst - np.mean(lst)) / np.std(lst)

def scale_minmax(lst):
    return (lst - np.min(lst)) / (np.max(lst) - np.min(lst))

def scale_maxabs(lst):
    return lst / np.max(np.abs(lst))

def scale_robust(lst):
    return (lst - np.median(lst)) / (np.quantile(lst, 0.75) - np.quantile(lst, 0.25))


df = [df1, df2, df3, df4]
scaler = [scaler1, scaler2, scaler3, scaler4]
scaled = [scale_standard(df1), scale_minmax(df2), scale_maxabs(df3), scale_robust(df4)]


def scaling_method_compare_plot(df=df, scaler=scaler):
    for df, scaler in zip(df, scaler):
        scaled_df = scaler.fit_transform(df)
        scaled_df = pd.DataFrame(scaled_df, columns=df.columns)

        _, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6, 5))

        ax1.set_title('Before Scaling')
        for x in df.columns:
            sns.kdeplot(df[x], ax=ax1)

        ax2.set_title('After Scaled')
        for x in df.columns:
            sns.kdeplot(scaled_df[x], ax=ax2)

        plt.show()


def scaling_function_compare_plot(df=df, func=scaled):
    for df, scaled in zip(df, func):
        scaled_df = pd.DataFrame(scaled, columns=df.columns)

        _, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6, 5))

        ax1.set_title('Before Scaling')
        for x in df.columns:
            sns.kdeplot(df[x], ax=ax1)

        ax2.set_title('After Scaled')
        for x in df.columns:
            sns.kdeplot(scaled_df[x], ax=ax2)

        plt.show()

