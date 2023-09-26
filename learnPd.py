import pandas as pd
# initialize data with null
data= {'Col1':['C', 'A', 'C', 'D'],
       'Col2':[1, 2, None , 4]}
df = pd.DataFrame(data)
df = df.set_index('Col1')
df = df.sort_index()
print(df)
print(df.loc[['A','C','D'], 'Col2'])
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