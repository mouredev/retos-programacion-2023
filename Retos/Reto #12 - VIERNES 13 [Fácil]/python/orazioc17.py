import datetime


def determine_friday_13(month: int, year: int) -> bool:
    day = datetime.date(year=year, month=month, day=13)
    return day.isoweekday() == 5


def run():
    print(determine_friday_13(3, 2023))  # False
    print(determine_friday_13(9, 2023))  # False
    print(determine_friday_13(10, 2023))  # True


if __name__ == '__main__':
    run()
