import pandas as pd
import numpy as np

data = {1: 1, 2: 2, 3:3}
ser = pd.Series(data)
ser = ser.sort_index(ascending=False)
print(ser)
# ser2 = ser[ser>= 2]
# myind = ser2.index
# print(myind[-1])

# # series = pd.Series([1, 0.9, 3, 0.89, 5])
# series = pd.Series({'A': np.array([1, 0.9, 3, 0.89, 5])})
# print(type(series))
# # mask = series>1
# print(series['A']> 1)


# initialize data with null
# data= {'Col1':['C', 'A', 'C', 'D'],
#        'Col2':[1, 2, None , 4]}
# df = pd.DataFrame(data)
# df = df.set_index('Col1')
# df = df.sort_index()
# print(df)
# print(df.loc[['A','C','D'], 'Col2'])
# ser = df.loc[['A','C'], 'Col2']
# print(pd.DataFrame(ser))
# print(type(df.iloc[0:3, 0:1]))
# df3 = df.iloc[0:3, 0:1]
# print(df3['Col2'])
# df.Col1 = df.Col1.replace({'A': 'AA'})
# df = df.dropna(how='all')

# df = df[df['Col2'].notna()]

# print(df.loc[0: 2, 'Col1': 'Col2'])
# print(df.iloc[0: 2, 0:1])
# lst = [0, 1, 2, 3]
# # print(lst[0:2])
# del df['Col1']
# df.drop(columns=['Col1', 'Col2'], inplace=True)
# print(df)