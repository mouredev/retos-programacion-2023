### Reto #14: OCTAL Y HEXADECIMAL ###
# MEDIA | Publicación: 03/04/23 | Resolución: 10/10/23

"""
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
"""

def octal_and_hex(entero: int):
            
    #octal
    current_int = entero
    octal = ""
    while current_int >= 0:
        octal = str(current_int % 8) +  octal
        current_int //=8
    
    octal=0 if octal == "" else octal 
    print(f"{entero} en Octal es {octal}")
    
    #hexadecimal
    current_int = entero
    hex_values = "0123456789ABCDEF"
    hex = ""
    while current_int >= 0:
        hex = hex_values[current_int % 16] +  hex
        current_int //=16
    
    hex=0 if hex == "" else hex 
    print(f"{entero} en Hexagesimal es {hex}")
    
octal_and_hex(15)
octal_and_hex(30)
octal_and_hex(50)