import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Catherine', 'Cahill', 'James', 'Emily', 'Michael', 'Monica', 'Laura', 'Kevin', 'Jordan'],
             'score': [13, 9.5, 16.5, np.nan, 11, 20, 17, np.nan, 8.5, 19],
             'attempts': [1, 3, 3, 2, 2, 3, 2, 3, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
# print(df)

print("##### 1-1. Select the 'name' and 'score' columns from the above DataFrame #####")
df1_1 = df[['name', 'score']]
print(df1_1)
print()

print("##### 1-2. Select first three rows of the DataFrame #####")
df1_2 = df.iloc[0:3]
print(df1_2)
print()

print("##### 1-3. Select 'name' and 'score' columns in rows 1, 2, 5, 6 from the following data frame #####")
df1_3 = df.loc[['b', 'c', 'f', 'g'], ['name', 'score']]
print(df1_3)
print()

print("##### 1-4. Select all columns whose attempts is larger then 2 #####")
df1_4 = df[df['attempts'] > 2]
print(df1_4)
print()

print("##### 2-1. Select the rows where the score is missing(NaN) #####")
df2_1 = df[df['score'].isnull()]
print(df2_1)
print()

print("##### 2-2. Select the rows where number of attempts in the examination is less than 2 and score greater than 15 #####")
df2_2 = df[(df['attempts'] < 2) & (df['score'] > 15)]
print(df2_2)
print()

print("##### 2-3. Calculate the sum of the examination attempts #####")
df2_3 = df['attempts'].sum()
print(df2_3)
print()

print("##### 2-4. Calculate the mean of the score #####")
df2_4 = df['score'].mean()
print(df2_4)
print()

print("##### 3-1. Append a new row 'k' to DataFrame with the given values for each column #####")
df_add = pd.DataFrame({'name': 'Saya', 'score': 17.5, 'attempts': 2, 'qualify': 'yes'}, index=['k'])
df3_1 = df.append(df_add)
print(df3_1)
print()

print("##### 3-2. Delete the new row and return the original data frame from above problem #####")
df3_2 = df3_1.drop('k', axis=0)
print(df3_2)
print()

print("##### 3-3. Delete 'attempts' column #####")
df3_3 = df3_2.drop('attempts', axis=1)
print(df3_3)
print()

print("##### 3-4. Get the sum of score group by 'attempts' #####")
df3_4 = df.groupby('attempts').sum()
print(df3_4)
print()

print("##### 4-1. Do inner join above df and below df2 #####")

exam2_data = {'name': ['Anastasia', 'Catherine', 'Ronaldo', 'James', 'Messi', 'Michael', 'Monica', 'Laura', 'Klassen', 'Jonas'],
              'score2': [11, 20, 16.5, np.nan, 10, 15, 20, np.nan, 8, 8]}
labels2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df2 = pd.DataFrame(exam2_data, index=labels2)

df4_1 = df.merge(df2, how='inner')
print(df4_1)
print()