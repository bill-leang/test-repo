import pandas as pd

data= {'age': [25,30,35,40,45,50,55,60,65]}
df = pd.DataFrame(data)

bins= [0,30,45,65,100] # the bin edges
labels= ['young', 'mature adult', 'middle-aged','snr'] # the label includes the bin ages

df['age_group'] = pd.cut(df['age'], bins=bins, labels= labels)
# qcut() is quantile cut, we specify the number of quantiles, and labels, pd will find the edges
df['qcut'] = pd.qcut(df['age'], q=4, labels=['first', 'second', 'third','fourth'])
print(df)