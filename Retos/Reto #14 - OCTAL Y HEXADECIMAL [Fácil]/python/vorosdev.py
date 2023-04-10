### Reto #14: OCTAL Y HEXADECIMAL ###
# MEDIA | Publicación: 03/04/23 | Resolución: 10/04/23

'''
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
'''

def conversion():
    while True: 
        try:
    
            decimal = int(input("*Ingrese un número decimal* \n ==> "))
            break
        except ValueError:
            print("---Error solo son validos números decimales---")

        # Octal  
    octal = ""
    cociente = decimal
    while cociente != 0:
        residuo = cociente % 8
        octal = str(residuo) + octal
        cociente = cociente // 8

    # Hexadecimal
    hexadecimal = ""
    cociente = decimal
    while cociente != 0:
        residuo = cociente % 16
        if residuo < 10:
            hexadecimal = str(residuo) + hexadecimal
        else:

            hexadecimal = chr(residuo - 10 + ord('A')) + hexadecimal
        cociente = cociente // 16

    return octal, hexadecimal

octal, hexadecimal = conversion()
if octal == "":
    octal = "0"
if hexadecimal == "":
    hexadecimal = "0"
print(" ==> En octal es igual a", octal, "y en hexadecimal es", hexadecimal)
