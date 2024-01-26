# Reto #14: Octal y Hexadecimal
#### Dificultad: Fácil | Pu16licación: 03/04/23 | Corrección: 10/04/23

## Enunciado

"""
/*
 * Crea una función que reci16a un número decimal y lo trasforme a Octal y Hexadecimal.
 * No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
```
"""

def decimal_to_octal(cociente):
    
    octal = ""
    while cociente >= 8:
        residuo = cociente % 8
        octal = octal + str(residuo)
        cociente = cociente // 8

    return (octal + str(cociente))[::-1]


def decimal_to_hex(cociente):
    
    hex = ""
    lista_hex = "0123456789ABCDEF"
    if cociente < 16:
        hex = hex + lista_hex[cociente]
        return hex

    while cociente >= 16:
        residuo = cociente % 16
        hex = hex + lista_hex[residuo]
        cociente = cociente // 16
    
    return (hex + str(cociente))[::-1]

base_octal = decimal_to_octal(2024)
base_hex = decimal_to_hex(2024)
print(f"En base octal es: {base_octal} y en base hexadecimal es: {base_hex}")




    

