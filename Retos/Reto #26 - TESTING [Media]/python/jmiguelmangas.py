"""
/*
 * Crea tres test sobre el reto 12: "Viernes 13".
 * - Puedes copiar una solución ya creada por otro usuario en
 *   el lenguaje que estés utilizando.
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección).
 */
"""

import datetime


def check_date_f13(date_given):
    x_date = datetime.date(
        int(date_given["year"]), int(date_given["month"]), int(date_given["day"])
    )
    no = x_date.weekday()

    if no != 4:
        return False
    else:
        return True


date1 = {"year": "2012", "month": "1", "day": "13"}
date2 = {"year": "2012", "month": "2", "day": "13"}
date3 = {"year": "2023", "month": "7", "day": "13"}
assert check_date_f13(date1) == True
assert check_date_f13(date2) == False
assert check_date_f13(date3) == False
