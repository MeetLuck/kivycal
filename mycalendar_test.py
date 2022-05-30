#calendar.MONDAY
#calendar.TUESDAY
#calendar.WEDNESDAY
#calendar.THURSDAY
#calendar.FRIDAY
#calendar.SATURDAY
#calendar.SUNDAY
#Aliases for day numbers, where MONDAY is 0 and SUNDAY is 6.

import calendar
year,month = 2022,5
weekday, numofdays = calendar.monthrange(year, month)
c = calendar.TextCalendar(calendar.SUNDAY)
row = 1
for year,month,day,weekday in c.itermonthdays4(year,month): 
    col = (weekday+1) % 7
    print(month,day,row,col) 
    if col == 6: row += 1
