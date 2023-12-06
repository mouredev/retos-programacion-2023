#!/usr/bin/env python3

import calendar

def is_there_13_friday(month, year, debug=False):
    cal = calendar.Calendar()

    if debug:
        print(calendar.month(year, month))

    for day in cal.itermonthdays2(year, month):
        if day[0] == 13:
            break

    if day[1] == calendar.FRIDAY:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_there_13_friday(1,1990))
    print(is_there_13_friday(1,2012))
    print(is_there_13_friday(3,1988))
    print(is_there_13_friday(4,2012))
    print(is_there_13_friday(3,1991))
    print(is_there_13_friday(7,2012))
    print(is_there_13_friday(6,2023))
    print(is_there_13_friday(3,2020))
