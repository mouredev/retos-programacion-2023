from datetime import datetime


def FridayThe13th(month, year):
    date = datetime(year, month, 13)

    return True if date.weekday() == 4 else False


print(f'Hay un viernes 13 en marzo de 2023? {FridayThe13th(3, 2023)}')
print(f'Hay un viernes 13 en octubre de 2023? {FridayThe13th(10, 2023)}')
