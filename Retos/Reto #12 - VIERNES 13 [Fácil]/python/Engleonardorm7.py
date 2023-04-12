# /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13
#  * en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */

import datetime

def is_friday_13th(month, year):
    date = datetime.date(year, month, 1)
    while date.month == month:
        if date.weekday() == 4 and date.day == 13:
            return True
        date += datetime.timedelta(days=1)

    return False

print(is_friday_13th(10, 2023))