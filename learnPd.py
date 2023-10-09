import pandas as pd
import numpy as np

# two ways to create a new col from an existing col
data = {'Label':['RU', 'US', 'CN'], 'Country': ['Russia', 'United States', 'China']}
df = pd.DataFrame(data)
df = df.set_index('Label')
# using iterrow()
for lab, row in df.iterrows():
    # it's IMPORTANT to use .loc here or the result will be unexpected
    df.loc[lab, "name_len"] = len(row.item())
# using .apply()
df['name_len'] = df['Country'].apply(len)
# print(df)
# print(df)

# data = {1: 1, 2: 2, 3:3}
# ser = pd.Series(data)
# ser = ser.sort_index(ascending=False)
# print(ser)

#########
# import numpy as np

# np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
# np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
# # array broadcasting
# bmi = np_weight / np_height **2
#  # filter like a Series
# bmi [ bmi >23]
# each API call returns only 10 results
# we can find the total number of results in the meta's value (hits), each page stores 10 results, offsets tell 
# us the location of the current page
# response_list[0]['response']['meta'] = {'hits': 12226, 'offset': 0, 'time': 34}
# loop through pages 0-2
# query = "Obama"
# begin_date="20120101"
# end_date = "20121231"
# response_list = []
# # to get 30 results we need to get 3 pages
# for i in range(3):
#     page = i
#     full_url= f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&begin_date={begin_date}&end_date={end_date}&page={page}&api-key={api_key}"
#     response_list.append(requests.get(full_url).json())
# from datetime import datetime
# # format 'pub_date': '2012-12-31T19:29:38+0000'
# date = dt.strptime(article['pub_date'], '%Y-%m-%dT%H:%M:%S%z')
# # print out the only the date part
# date.date()
# tum_df = pd.concat([tum_mean, tum_median, tum_var, tum_std, tum_stderr], axis=1, keys= col_names)
# # change box border color, whisker color, capline color, median line color, and outlier color
# box_df.plot(kind='box', ylabel='Final Tumor Volume (mm3)', boxprops={'color': 'black', 'linewidth': 1}, \
#            whiskerprops = {'color': 'black'}, capprops= {'color': 'black'}, medianprops= {'markerfacecolor': 'orange'},\
#            flierprops={'markerfacecolor': 'red', 'markersize': 11})

# import numpy as np
# from sklearn.linear_model import LinearRegression
# X = capo_scat_df['Weight (g)'].values.reshape(-1,1)
# Y = capo_scat_df['Tumor Volume (mm3)'].values

# model = LinearRegression()
# model.fit(X,Y)

# Y_pred = model.predict(X)
# capo_scat_df.plot(kind='scatter', x='Weight (g)', y='Tumor Volume (mm3)', s=50)
# # plot the regression line
# plt.plot(X, Y_pred, color='red', label='Regression Line')
# plt.show()

# calc two columns from groupby
# capo_scat_df = pd.DataFrame(capo_df.groupby('Mouse ID')[['Weight (g)','Tumor Volume (mm3)']].mean())

# plot scatter plot with increased marker size
# capo_scat_df.plot(kind='scatter', x='Weight (g)', y='Tumor Volume (mm3)', s=50)
# merged_df = pd.merge(all_data_unique, mouse_last_timepoint, right_index= True, left_on='Mouse ID', suffixes=['', '_greatest'])

# ax = all_data_unique.groupby('Drug Regimen')[['Mouse ID']].count().sort_values(by='Mouse ID', ascending=False).plot(kind='bar', legend=False)
# ax.set_ylabel('# of Observed mouse Timepoints')
# plt.show()

# count_df = all_data_unique.groupby('Drug Regimen')[['Mouse ID']].count().sort_values(by='Mouse ID', ascending=False)
# plt.bar(count_df.index, count_df['Mouse ID'])
# plt.xticks(count_df.index, count_df.index, rotation='vertical')
# plt.ylabel('# of Observed Mouse Timepoints')
# plt.xlabel('Drug Regimen')

#######


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