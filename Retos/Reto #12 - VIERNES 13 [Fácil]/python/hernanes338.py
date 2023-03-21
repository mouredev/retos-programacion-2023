import calendar

def isFriday13(month: int, year: int):
    days_of_month = calendar.monthcalendar(year, month)
    fridays_of_month = list(days_of_month[i][4] for i in range(len(days_of_month)))
    if 13 in fridays_of_month:
        return True
    else:
        return False

print(isFriday13(3,2023)) # False
print(isFriday13(3,2020)) # True