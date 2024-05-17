"""
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
"""

from datetime import date, time, datetime

def friday_thirteen():
    """
    This function takes a month and a year and determines if there was a 13 friday.

    Args:
    month(str): any month
    year(str): any year

    Returns:
    bool: returns if it had been a 13 friday at that date.

    """
    month = input("Ingrese un mes (mm): ")
    year = input("Ingrese un año (yyyy): ")

    if len(month) == 2 and len(year) == 4:
        date_check = datetime.strptime('13'+month+year, '%d%m%Y')
        weekday = date_check.weekday() # returns the number of the week day. Starts at monday with '0'

        if weekday == 4:
            return True
        return False
    else:
        print("Las fechas no son validas")

print(friday_thirteen())