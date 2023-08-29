# código de la función le pertenece a @jcdm60
# disponible en: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2312%20-%20VIERNES%2013%20%5BF%C3%A1cil%5D/python/jcdm60.py

import datetime


def is_friday_13(month, year):

    # Creamos un objeto datetime para el 13 del month y año indicados
    date = datetime.date(year, month, 13)

    # Comprobamos si es viernes (el número 4 representa el día viernes)
    if date.weekday() == 4:
        return True
    else:
        return False


def test_is_friday_13():
    tests = {'input': [[4, 2022], [8, 2024], [5, 2022], [
        9, 2024]], 'output': [False, False, True, True]}
    errors = 0

    for index, test in enumerate(tests['input']):
        resp = is_friday_13(test[0], test[1])
        expected = tests['output'][index]
        if resp != expected:
            errors += 1
            print(f"\n\noriginal: {test}")
            print(resp)
            print(f"expected: {expected}")

    print(
        f"\nTests{' not ' if errors != 0 else ' '}passed, {errors} errors\n")


test_is_friday_13()
