import datetime

def isThereAnyFriday13th(month, year):
    return datetime.date(year, month, 13).weekday() == 4

print(isThereAnyFriday13th(10, 2023))