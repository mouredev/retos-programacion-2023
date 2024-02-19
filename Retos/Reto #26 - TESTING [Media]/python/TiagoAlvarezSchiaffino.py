import datetime

def check_is_friday_13(date_given):
    """
    Check if a given date falls on a Friday the 13th.

    Args:
        date_given (dict): Dictionary with keys "year", "month", and "day" representing the date.

    Returns:
        bool: True if the given date is a Friday the 13th, False otherwise.
    """
    x_date = datetime.date(
        int(date_given["year"]), int(date_given["month"]), int(date_given["day"])
    )
    return x_date.weekday() == 4

# Test 1:
date1 = {"year": "2012", "month": "1", "day": "13"}
assert check_is_friday_13(date1) == True

# Test 2:
date2 = {"year": "2012", "month": "2", "day": "13"}
assert check_is_friday_13(date2) == False

# Test 3:
date3 = {"year": "2023", "month": "7", "day": "13"}
assert check_is_friday_13(date3) == False
