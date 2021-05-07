# 1. Write a Python script to display the various Date Time formats - Go to the editor

# a) Current date and time
import datetime

x = datetime.datetime.now()
print(x)
# b) Current year
print(x.year)
# c) Month of year
print(x.month)
# d) Week number of the year
print(x.strftime("%U"))
# e) Weekday of the week
print(x.strftime("%A"))
# f) Day of year
print(x.strftime("%j"))
# g) Day of the month
print(x.strftime("%d"))
# h) Day of week
print(x.strftime("%w"))