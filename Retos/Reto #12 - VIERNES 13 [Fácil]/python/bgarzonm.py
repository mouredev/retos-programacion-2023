from datetime import datetime


def has_friday_13(year: int, month: int) -> bool:
    """Check if a date is friday 13th

    Args:
        year (int):
        month (int):

    Returns:
        bool:
    """
    return datetime(year, month, 13).weekday() == 4


if __name__ == "__main__":
    print(has_friday_13(2020, 3))
