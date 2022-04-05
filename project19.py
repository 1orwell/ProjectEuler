# Includes 1900!! Just remove this.

days_per_month = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31,
 'jun': 30, 'jul': 31, 'aug': 31, 'sep': 30, 'oct': 31, 'nov': 30, 'dec': 31}

day_map = {0 : 'Mon', 1 : 'Tue', 2 : 'Wed', 3 : 'Thu', 4 : 'Fri', 5 : 'Sat', 6 : 'Sun'}
month_map = {0 : 31, 1 : 28, 2 : 31, 3 : 30, 4 : 31, 5 : 30,
            6 : 31, 7 : 31, 8 : 30, 9 : 31, 10 : 30, 11 : 31}
month_map_day = {0 : 'jan', 1 : 'feb', 2 : 'mar', 3 : 'apr', 4 : 'may', 5 : 'jun',
            6 : 'jul', 7 : 'aug', 8 : 'sep', 9 : 'oct', 10 : 'nov', 11 : 'dec'}

def day_next_month_begins(year, prev_month, current_start_day):
    #could be a leap year
    days_in_month = 0
    print(f'current month is {prev_month}')
    if prev_month == 1:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    days_in_month = 29
                else: 
                    days_in_month = 28
            else: 
                days_in_month = 29
        #not a leap year
        else:
            days_in_month = 28
    else:
        days_in_month = month_map[prev_month]

    days_over = days_in_month % 7
    # %7 makes it loop back to 0 for Monday
    return((current_start_day + days_over)%7)
    

total_sundays = 0
start_day = 0

for year in range(1900, 2001):
    for month in range(0, 12):
        # 1900 is divisible by 4, but not 400, therefore not a leap year.
        print(year, month_map_day[month])
        print(f'This month starts on a {day_map[start_day]}')
        if start_day == 6:
            total_sundays += 1
            print(f'The start of this month is a Sunday, {total_sundays} Sundays so far.')
        start_day = day_next_month_begins(year, month, start_day)

print(total_sundays)
