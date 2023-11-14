import datetime

# print(help(datetime.timedelta))

#####DATE#####
d = datetime.date(2016, 7, 24) # do not add leading zeroes in dates
print(d)

tday = datetime.date.today()
print(tday.year)
print(tday.weekday())
print(tday.isoweekday()) # for ISO Weekday Monday is 1

# Time Deltas
tdelta = datetime.timedelta(days=7)
print(tday - tdelta)

# date2 = date1 + timedelta # if we add or subract timedelta from a date we get a date
# timedelta = date1 + date2 # if we add or subract two dates then we get a timedelta

# calculate how many days remaining for my birthday
bday = datetime.date(2024, 2, 11)
till_bday = bday - tday

print(till_bday.days)

#####TIME#####

t = datetime.time(9, 30, 45, 1000)
print(t.hour)

#####DATE & TIME#####
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)

tdelta = datetime.timedelta(hours = 12)
print(dt + tdelta)

tday = datetime.datetime.today() # current local datetime with timezone as none
tday_now = datetime.datetime.now() # gives option to put timezone
tday_utcnow = datetime.datetime.utcnow() # current UTC time

print(tday)
print(tday_now)
print(tday_utcnow)

print("######### Using PYTZ #########")
import pytz
dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

tday_now = datetime.datetime.now(tz=pytz.UTC)
print(tday_now)

tday_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(tday_utcnow)

# converting to diff timezone
dt_mtn = tday_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

dt = datetime.datetime.now()
dt_east = dt.astimezone(pytz.timezone('US/Mountain'))
print(dt_east)

# for tz in pytz.all_timezones:
# 	print(tz)

# ISO format
tday_now = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(tday_now.isoformat())

# Converting to date formats
print(tday_now.strftime('%B %d, %Y'))

# converting string to datetime
dt_str = 'November 13, 2023'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime






