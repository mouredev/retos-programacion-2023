# Reto #28: Expresión matemática
#### Dificultad: Media | Publicación: 10/07/23 | Corrección: 17/07/23

## Enunciado


#
# Crea una función que reciba una expresión matemática (String)
# y compruebe si es correcta. Retornará true o false.
# - Para que una expresión matemática sea correcta debe poseer
#   un número, una operación y otro número separados por espacios.
#   Tantos números y operaciones como queramos.
# - Números positivos, negativos, enteros o decimales.
# - Operaciones soportadas: + - # / % 
#
# Ejemplos:
# "5 + 6 / 7 - 4" -> true
# "5 a 6" -> false
#

import re

class ExpresionMatematica:
    def __init__(self, expresion):
        self.expresion = expresion
        self.componentes = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+|\S', expresion)
    
    def validar_expresion(self):
        if len(self.componentes) < 3 or len(self.componentes) % 2 != 1:
            return False

        for i in range(0, len(self.componentes), 2):
            numero = self.componentes[i]
            if not self.es_numero_valido(numero):
                return False

        operaciones_permitidas = ['+', '-', '*', '/', '%']
        for i in range(1, len(self.componentes), 2):
            operacion = self.componentes[i]
            if operacion not in operaciones_permitidas:
                return False

        return True
    
    def es_numero_valido(self, numero):
        try:
            float(numero)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    exp1 = ExpresionMatematica("5.66 + 6 / 7 - 4")
    print(exp1.validar_expresion())  # True

    exp2 = ExpresionMatematica("5 a 6")
    print(exp2.validar_expresion())  # False

    exp3 = ExpresionMatematica("8 * 2 * 3 - 4 / -2")
    print(exp3.validar_expresion())  # True

    exp4 = ExpresionMatematica("8 % 3 - 99")
    print(exp4.validar_expresion())  # True

