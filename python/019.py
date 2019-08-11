def is_leapyear(year):
    """ Tests whether year is a leap year """

    # A leap year occurs on any year evenly divisible by 4...
    if year % 4 == 0:
        # ...but not on a century...
        if year % 100 == 0:
            # unless it is divisible by 400.
            if year % 400 == 0:
                return True
            return False
        return True
    return False


days_in_month = {1: 31, 2: 28, 3: 31,
                 4: 30, 5: 31, 6: 30,
                 7: 31, 8: 31, 9: 30,
                 10: 31, 11: 30, 12: 31}

day, month, year = 1, 1, 1900 # Monday 1 January 1900
# day is a Sunday if it is divisble by 7

day += 365 + is_leapyear(year) # 1 January 1901
year += 1
count = 0 # number of Sundays
while year < 2001:
    count += (day % 7 == 0)

    day += days_in_month[month] # start of next month
    month += 1
    if month == 3: # March; last month was February
        day += is_leapyear(year) # include 29 February
    elif month > 12: # next year
        month = 1
        year += 1

print(count)
