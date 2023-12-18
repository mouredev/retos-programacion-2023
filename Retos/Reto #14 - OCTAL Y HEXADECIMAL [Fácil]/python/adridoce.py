"""
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
"""

def octal(numero):
    try:
        numero_entero = int(numero)
        es_negativo = numero_entero < 0
        numero_entero = abs(numero_entero)
        resultado_octal = ""

        while numero_entero > 0:
            residuo = numero_entero % 8
            resultado_octal = str(residuo) + resultado_octal
            numero_entero //= 8

        # Agrega el prefijo "0o" y el signo si es negativo
        resultado_octal = "0o" + resultado_octal
        if es_negativo:
            resultado_octal = "-" + resultado_octal

        return resultado_octal
    except ValueError:
        return "Error: Por favor, proporciona un número entero como argumento."


def hexadecimal(numero):
    try:
        numero_entero = int(numero)
        es_negativo = numero_entero < 0
        numero_entero = abs(numero_entero)
        caracteres_hexadecimales = "0123456789ABCDEF"
        resultado_hexadecimal = ""

        while numero_entero > 0:
            residuo = numero_entero % 16
            resultado_hexadecimal = caracteres_hexadecimales[residuo] + resultado_hexadecimal
            numero_entero //= 16

        # Agrega el prefijo "0x" y el signo si es negativo
        resultado_hexadecimal = "0x" + resultado_hexadecimal
        if es_negativo:
            resultado_hexadecimal = "-" + resultado_hexadecimal

        return resultado_hexadecimal
    except ValueError:
        return "Error: Por favor, proporciona un número entero como argumento."



print(octal(100))
print(octal(1000))
print(hexadecimal(100))
print(hexadecimal(1000))