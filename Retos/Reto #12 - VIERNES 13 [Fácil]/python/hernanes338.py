import calendar

def isFriday13(month: int, year: int):
    days_of_month = calendar.monthcalendar(year, month)
    fridays_of_month = list(days_of_month[i][4] for i in range(len(days_of_month)))
    if 13 in fridays_of_month:
        return f"There is a Friday 13 on {month}/{year}"
    else:
        return f"There is no Friday 13 on {month}/{year}"


## Start program execution ##

print(isFriday13(3,2023)) # There is no Friday 13 on 3/2023
print(isFriday13(3,2020)) # There is a Friday 13 on 3/2020

## End program execution ##