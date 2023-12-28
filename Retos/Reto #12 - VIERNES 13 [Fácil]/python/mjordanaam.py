"""
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
"""
import datetime

DAY = 13


def friday_13(year: int, month: int) -> bool:
	if year >= 0 and 0 < month < 13:
		x = datetime.date(year, month, DAY)
		if x.strftime("%u") == '5':
			return True

	return False


print(friday_13(2023, 3))  # False
print(friday_13(2023, 5))  # False
print(friday_13(2023, 1))  # True
print(friday_13(2023, 10))  # True
print(friday_13(2022, 5))  # True
print(friday_13(2026, 3))  # True
print(friday_13(2021, 8))  # True
print(friday_13(-2021, 8))  # False
print(friday_13(2023, -8))  # False
print(friday_13(2023, 13))  # False
print(friday_13(2023, 64))  # False
