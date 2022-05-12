#!/usr/bin/python3

from datetime import datetime

#set the date and time format
date_format = "%m-%d-%Y %H:%M:%S"

#convert string to actual date and time
time1  = datetime.strptime('8-01-2008 00:00:00', date_format)
time2  = datetime.strptime('8-02-2008 01:30:00', date_format)

#find the difference between two dates
diff = time2 - time1


''' days and overall hours between two dates '''
print(time1)
print(time2)
print ('Days & Overall hours from the above two dates')
#print days
days = diff.days
print (str(days) + ' day(s)')

#print overall hours
days_to_hours = days * 24
diff_btw_two_times = (diff.seconds) / 3600
overall_hours = days_to_hours + diff_btw_two_times
print (str(overall_hours) + ' hours');

a = datetime.datetime.now()
b = datetime.datetime(2015,8,25,0,0,0,0)
c = a - b
print(f'{c.total_seconds()}')
# 87062.729491
print(f'{c.total_seconds() > 3*3600}')
#True


''' now print only the time difference '''
''' between two times (date is ignored) '''

print ('\nTime difference between two times (date is not considered)')

#get hours, minutes, seconds from total seconds
seconds = 23562
hours, remainder = divmod(seconds, 3600)
minutes, seconds = divmod(remainder, 60)
# or
minutes, seconds = divmod(int(seconds), 60)
hours, minutes = divmod(minutes, 60)


