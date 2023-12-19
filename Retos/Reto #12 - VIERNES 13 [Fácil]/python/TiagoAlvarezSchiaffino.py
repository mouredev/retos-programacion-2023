import datetime

def is_friday_13(year: int, month: int) -> bool:
    """
    Check if there is a Friday the 13th in the given month and year.

    Args:
        year (int): The year.
        month (int): The month.

    Returns:
        bool: True if there is a Friday the 13th, False otherwise.
    """
    try:
        return datetime.date(year, month, 13).weekday() == 4
    except ValueError:
        return False

# Examples
print(is_friday_13(2023, 5))
print(is_friday_13(2023, 1))
print(is_friday_13(2023, 13))
print(is_friday_13(-2023, 1))