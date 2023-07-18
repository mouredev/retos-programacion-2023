"""
* Crea tres test sobre el reto 12: "Viernes 13".
 * - Puedes copiar una solución ya creada por otro usuario en
 *   el lenguaje que estés utilizando.
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección). 
"""

import datetime
#Lemito66
def friday_thirteen(year: int, month: int) -> bool:
    try:
     return datetime.date(year,month,13).weekday() == 4 # weekday() return day of the week, where Monday == 0 ... Sunday == 6.
    except: 
        return False

print(friday_thirteen(2023,10))