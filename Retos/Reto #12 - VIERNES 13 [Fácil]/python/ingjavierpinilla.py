from datetime import datetime


def has_friday_13(year: int, month: int) -> bool:
    """Esta funcion retorna verdadero si para un año y mes dado existe un viernes 13

    Args:
        year (int):
        month (int):

    Returns:
        bool:
    """
    return datetime(year, month, 13).weekday() == 4


if __name__ == "__main__":
    print(has_friday_13(2023, 1))
