'''
 Crea una función que reciba una expresión matemática (String)
 y compruebe si es correcta. Retornará true o false.
 - Para que una expresión matemática sea correcta debe poseer
   un número, una operación y otro número separados por espacios.
   Tantos números y operaciones como queramos.
 - Números positivos, negativos, enteros o decimales.
 - Operaciones soportadas: + - * / % 
 Ejemplos:
 "5 + 6 / 7 - 4" -> true
 "5 a 6" -> false
'''

valid_operation = ['+', '-', '*', '/', '%']

def check_math(expression: str) -> bool:
    items = expression.split(' ')
    
    for pos in range(0, len(items)):
        if(pos % 2 == 0):
            try:
                float(items[pos])
            except Exception:
                return False
        else:
            if items[pos] not in valid_operation:
                return False
    
    return True

print(check_math('5 + 6 / 7 - 4')) # correct
print(check_math('5 a 6')) # incorrect
print(check_math('5.3 / 6')) # correct
print(check_math('5.3 / a')) # incorrect
print(check_math('8 / -2')) # correct
print(check_math('+ 3 - 2')) # incorrect