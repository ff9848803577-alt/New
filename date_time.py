# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime 

x = datetime.datetime.now()

print(x)

# to onlt print the year and the name of weekday 

import datetime 

y = datetime.datetime.now()

print(y.year)
print(y.strftime("%A"))