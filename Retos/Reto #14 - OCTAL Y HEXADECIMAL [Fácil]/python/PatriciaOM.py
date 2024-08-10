"""
Crea una función que reciba un número decimal y lo trasforme a Octal
y Hexadecimal.
No está permitido usar funciones propias del lenguaje de programación que
realicen esas operaciones directamente.
"""

def decimal_octal_hexadecimal(number):
    user_number = number
    octal = list()
    hexadecimal = list()
    #Octal
    while number > 0:
        octal.append(str(number % 8))
        number = number // 8 #cambiamos al nuevo valor
    octal.reverse() #le damos la vuelta para conseguir el orden correcto
    octal_str = ''.join(octal) #lo convertimos en string para imprimir
    #Hexadecimal
    while user_number > 0:
        module = user_number % 16
        if module == 10:  
            hexadecimal.append("A")
        elif module == 11:
            hexadecimal.append("B")
        elif module == 12:
            hexadecimal.append("C")
        elif module == 13:
            hexadecimal.append("D")
        elif module == 14:
            hexadecimal.append("E")
        elif module == 15:
            hexadecimal.append("F")
        else:
            hexadecimal.append(str(module))
        user_number = user_number // 16
    hexadecimal.reverse()
    hexadecimal_str = ''.join(hexadecimal)
    print(octal_str)
    print(hexadecimal_str)
    
decimal_octal_hexadecimal(4634534)