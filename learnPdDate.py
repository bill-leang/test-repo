import pandas as pd

rides = pd.read_csv('Resrc/bikes.csv', parse_dates=['Start date', 'End date'])

print(rides.head())
# # or convert the col to date manually, we can omit format
rides['Start date'] = pd.to_datetime(rides['Start date'], format='%Y-%m-%d %H:%M:%S')

# find the % of time the bike is used over the period of the data (91 days)
rides['Duration'].sum() / timedelta(days=91) 

# doing a groupby with date column, 'M' is for months on the 'Start date' col
# this will ouput the average duration for each month
# 'D' is for Day
rides.resample('D', on = 'Start date')['Duration seconds'].mean().plot()

rides.groupby('Member type').size()

rides.groupby('Member type').mean()

rides['Start date'] = rides['Start date']\
                    .dt.tz_localize('America/New_York', ambiguous='NaT')

# return the year of the date
rides['Start date'].dt.year
# return day name of the date, eg. Sunday
rides['Start date'].day_name()
# shift row down by 1, first row (0) will become NaT
rides['End date'].shift(1)