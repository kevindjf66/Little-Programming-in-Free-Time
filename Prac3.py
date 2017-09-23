'''
enter year, month and day to caculate which day it is in the year
'''

# enter year, month and day
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))
 
# record the number of days at the beginning of every month
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
#in case some wrong numbers were entered
else:
    print 'data error'
#
sum += day
leap_year = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap_year = 1
if (leap_year == 1) and (month > 2):
    sum += 1
print 'it is the %dth day.' % sum
