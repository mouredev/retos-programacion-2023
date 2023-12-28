import datetime


def friday_13(year: int, month: int) -> bool:
    try:
        return datetime.date(year, month, 13).weekday() == 4
    except:
        return False


print(friday_13(2023, 3))
print(friday_13(2023, 1))
print(friday_13(2023, 13))
print(friday_13(-2023, 1))
print(friday_13(2023, "1"))
print(friday_13(2023, 0))
print(friday_13("Brais", "Moure"))
