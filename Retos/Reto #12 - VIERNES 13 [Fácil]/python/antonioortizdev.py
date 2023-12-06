import calendar
import datetime


def is_friday_thirteen(year: int, month: int) -> bool:
    FRIDAY = 4
    date = datetime.date(year, month, 13)
    weekday = date.weekday()
    return weekday == FRIDAY


def print_all_friday_thirteens_to_year(to_year: int = datetime.date.today().year):
    for year in range(1970, to_year + 1):
        for month in range(1, 12):
            if is_friday_thirteen(year, month):
                print(
                    f'{calendar.month_name[month]} {year} has a Friday 13th!')


def main():
    print_all_friday_thirteens_to_year(2077)


main()
