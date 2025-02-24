# /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */

import calendar
from datetime import date, timedelta

def main():
    print("\nBienvenid@! confirmemos si hay algun viernes 13 en el mes del año que elijas: \n")
    while (True):
        year = input('Año: ')
        month = input('Mes: ')

        if year.isdigit() and month.isdigit():
            year = int(year)

            if month.isdigit() and 1 <= int(month) <= 12:
                month = int(month)
                break
            else:
                print('Mes no valido, intenta de nuevo')
        
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    _, num_days = calendar.monthrange(year, month)

    for day in range(1, num_days + 1):
        if date(year, month, day).weekday() == week_days.index('Friday') and day == 13:
            print(f'El viernes 13 de {month}/{year} existe!')
            break
        elif day == num_days:
            print(f'El viernes 13 de {month}/{year} no existe!')
    
main()
