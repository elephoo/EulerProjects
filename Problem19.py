import datetime
from dateutil.relativedelta import relativedelta
from calendar import weekday

from dateutil.relativedelta import relativedelta


#1 Jan 1900 was a Monday.

# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400

def first_of_month():
    count = 0
    date = datetime.date(1901, 1, 1)
    end_date = datetime.date(2000, 12, 31)
    while date <= end_date:
        if date.weekday() == 6:
            count += 1
        date += relativedelta(months= 1)
    return count

print(first_of_month())