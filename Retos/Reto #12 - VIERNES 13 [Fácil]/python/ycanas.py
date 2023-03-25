import datetime

def has_friday_thirteenth(month: int, year: int) -> bool:
    FRYDAY = 4
    DAY = 13

    date = datetime.date(year, month,  DAY)
    result = date.weekday() == FRYDAY
    return result


print(has_friday_thirteenth(3, 2023))
print(has_friday_thirteenth(10, 2023))
