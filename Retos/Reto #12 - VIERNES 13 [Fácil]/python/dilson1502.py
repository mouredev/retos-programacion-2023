from datetime import datetime

def is_friday_13(year: int,month: int) -> bool:
    """This func returns true if in a specified month in a year there is a friday 13

    Args:
        year (int): example 2023
        month (int): example 1022

    Returns:
        bool: _description_
    """
    return datetime(year,month,13).weekday() ==4
        
## sss

if __name__ == '__main__':
    print(is_friday_13(2024,10))
