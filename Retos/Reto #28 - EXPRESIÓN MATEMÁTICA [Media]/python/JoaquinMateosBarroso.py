import re

def checkMathExpression(expresion: str) -> bool:
    """Crea una función que reciba una expresión matemática (String)
    y compruebe si es correcta. Retornará true o false.
    - Para que una expresión matemática sea correcta debe poseer
    un número, una operación y otro número separados por espacios.
    Tantos números y operaciones como queramos.
    - Números positivos, negativos, enteros o decimales.
    - Operaciones soportadas: + - * / % 
    Ejemplos:
    "5 + 6 / 7 - 4" -> true
    "5 a 6" -> false"""
    return re.match(r'[+-]?[0-9]*[.]?[0-9]*\ [+-\/\*]\ [0-9]*[.]?[0-9]*', expresion) != None



print(checkMathExpression("3 + 5"))
print(checkMathExpression("3 a 5"))
print(checkMathExpression("-3 + 5"))
print(checkMathExpression("- 3 + 5"))
print(checkMathExpression("-3 a 5"))
print(checkMathExpression("-3+5"))
print(checkMathExpression("3 + 5 - 1 / 4 % 8"))