from datetime import datetime


def check_friday(month: int, year: int) -> bool:
    day = datetime(year=year, month=month, day=13)
    return day.weekday() == 4


print(check_friday(1, 2023))
print(check_friday(2, 2023))
