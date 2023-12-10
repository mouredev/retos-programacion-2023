from datetime import datetime

def isFriday13(date: list [int]) -> bool:
    week_day = datetime.weekday(datetime(date[1], date[0], 13))
    if week_day == 4:
        is_friday_13 = True
    else:
        is_friday_13 = False

    return is_friday_13

if __name__ == '__main__':
    print(isFriday13([11, 2015]))
    print(isFriday13([12, 2023]))
    