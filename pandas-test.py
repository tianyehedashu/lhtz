import pandas as pd
import numpy as np

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
data2 = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [0, 1, 1]}
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

# print(df1);
# print(df2);


df = pd.DataFrame({'AAA': [4, 5, 6, 7],
                   'BBB': [10, 20, 30, 40],
                   'CCC': [100, 50, -30, -50]})
df.loc[df.AAA < 5, ['BBB', 'CCC']] = 2000
df.loc[df.AAA < 5, ['logic']] = 3000
# print(df)
df['logic'] = np.where(df['AAA'] > 5, 'high', 'low')
# print(df)

df2 = pd.DataFrame({'AAA': [True] * 4, 'BBB': [False] * 4, 'CCC': [True, False] * 2})
test1 = df.loc[(df['BBB'] < 55),  'AAA']

test2 = df.loc[(df['BBB'] < 25) & (df['CCC'] >= -40), ['AAA', 'BBB']]

Crit1 = df.AAA <= 5.5

df = pd.DataFrame({'AAA': [1, 2, 1, 3],'BBB': [1, 1, 2, 2], 'CCC': [2, 1, 3, 1]})
source_cols = df.columns
new_cols = [str(x) + "_cat" for x in source_cols]
categories = {1: 'Alpha', 2: 'Beta', 3: 'Charlie'}
df['test'] = df['AAA'].map(categories.get)
df[new_cols] = df[source_cols].map(categories.get)
# print(new_cols)
print(df.index)

# print(Crit1)

# print(test1)

# print(test2)
