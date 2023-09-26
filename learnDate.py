
# from datetime import date

# from datetime import datetime, timedelta, timezone
# # set eastern time zone
# ET = timezone(timedelta(hours=-5))
# # add timezone to dt
# dt = datetime(2017,12,30,15,9,3, tzinfo=ET) 
# print(dt) #2017-12-30 15:09:03-05:00

# # India Standard time
# IST = timezone(timedelta(hours=5, minutes=30))
# print(dt.astimezone(IST)) # display dt in IST

# dt1 =dt.replace(tzinfo=timezone.utc)
# dt2 = dt.astimezone(timezone.utc)
# print(f'{dt1} ,{dt2}')

# from datetime import datetime
# from dateutil import tz
# first_1am = datetime(2017, 11, 5, 1, 0, 0, tzinfo=tz.gettz('US/Eastern'))
# # utc = tz.gettz('Europe/London')
# utc = tz.UTC
# print(tz.datetime_ambiguous(first_1am)) # True, meaning daylight saving happens, so there were two 1 am
# second_1am = tz.enfold(first_1am) # we get the 2nd 1am
# print(second_1am)
# print(second_1am.astimezone(utc) - first_1am.astimezone(utc)) # correct way to calc the difference
# et = tz.gettz('America/New_York') # format is Continent/City
# before_dls = datetime(2017,3,12,1,59,59, tzinfo=et)
# after_dls = datetime(2017,3,12,3,0,0, tzinfo=et)
# # t = after_dls - before_dls # will give us 1 hr 1s
# # after converting to UTC, it'll give us the absolute time difference, 1s
# t = after_dls.astimezone(tz.gettz('Europe/London')) - before_dls.astimezone(tz.gettz('Europe/London'))
# print(t.seconds)
# print(f'{after_dls} - {before_dls}') 

# # arguments are year, month, day, hh, mm, sec, microsec)
# dt = datetime(2023, 9, 8, 15, 3, 5, 500000) 
# print(dt.strftime('%Y/%m/%d %H:%M:%S')) 
# # %Y is 4 digit year, %m is two digit month, %d is two digit day, %H is 24-hour hour, %M is 2 digit min, %S is 2 digit sec
# # %h is month in three letters, %y is 2 digit year

# dt_new = dt.replace(minute=0, second=0, microsecond=0) # no inplace argument

# Starting string, in YYYY-MM-DD HH:MM:SS format
# s = '2017-2-4 00:00:01'
# # Write a format string to parse s
# fmt = '%Y-%m-%d %H:%M:%S'
# # Create a datetime object d
# d = datetime.strptime(s, fmt)
# print(d)
# s2 = '1/2/2018'
# fmt2 = '%m/%d/%Y'
# d2 = datetime.strptime(s2, fmt2)
# print(d2)

# ts = 2147483648
# dts = datetime.fromtimestamp(ts)
# print(dts)

# delta = timedelta(days=1, seconds=1) # can also be negative, eg. weeks=-1
# end = start + delta
# # initializing a date
# andrew = date(1992,8,24)
# # get day of the week 0: Monday, 6: Sunday
# print(f'day of week: {andrew.weekday()}')
# print(f'month: {andrew.month}') # .year, .day


# start = date(2007, 5, 9)
# end = date(2007, 12, 13)
# delta =end - start
# print(delta.days)

# A dictionary to count hurricanes per calendar month
# hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
# 		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}

# # Loop over all hurricanes
# for hurricane in florida_hurricane_dates:
#   # Pull out the month
#   month = hurricane.month
#   # Increment the count in your dictionary by one
#   hurricanes_each_month[month] += 1