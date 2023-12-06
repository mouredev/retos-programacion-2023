#
# Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
# - La función recibirá el mes y el año y retornará verdadero o falso.
#

from datetime import date


def friday13(year, month):
    return date(year, month, 13).weekday() == 4


if __name__ == "__main__":
    test_values = [True, False, False, False, False,
                   False, False, False, False, True, False, False]
    for i in range(1, 13):
        assert friday13(
            2023, i) == test_values[i-1], f"Month {i} should be {test_values[i-1]}"
