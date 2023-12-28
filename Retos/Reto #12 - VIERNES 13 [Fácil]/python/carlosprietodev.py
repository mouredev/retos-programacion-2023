"""
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
"""

import calendar


def friday(month:int,year:int):
    if calendar.weekday(year,month,13)== 4: # Como se empieza a contar desde 0, el Viernes es el nº 4. Por tanto, se realiza
                                            # una condicion en la que si el mes y el año que se quiere comprobar, con la fecha 13 es igual a Viernes
        return True                         # se devuelve True y en caso contrario se devuelve False.
                                            
    else:
        return False
    

print(friday(5,2022))
print(friday(1,2500))