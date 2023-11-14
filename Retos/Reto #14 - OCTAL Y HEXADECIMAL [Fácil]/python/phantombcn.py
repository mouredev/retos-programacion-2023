''' ENUNCIADO
    Crea una función que reciba un número decimal y lo trasforme a Octal
    y Hexadecimal.
    - No está permitido usar funciones propias del lenguaje de programación que 
    realicen esas operaciones directamente.
'''

'''
    Este programa convierte un numero en base decimal a base octal y base hexadecimal.
    El numero debe ser entero
    En el caso de números negativos al número convertido se le pone el signo - delante
    Autor (GitHub) : PhantomBCN
    Versión: 1.0
    Fecha: 4 de abril de 2023
'''

# Define una función para solicitar un número decimal al usuario y asegurarse de que sea válido
def solicitar_decimal():
    while True:
        try:
            n_decimal = int(input("Introduce un número en decimal: "))
            return n_decimal
        except ValueError:
            print("Debe introducir un número sin decimales.")


'''
    Funcion que hace la conversión a octal (8) o hexadecimal (16) segun se pase el parámetro base
    En el caso de pasaro un valor diferente a 8 o 16 devolverá un texto con el error
'''

def cambio_de_base (n_decimal, base):

    letras_hexa = {10 : 'A', 11 : 'B', 12 : 'C', 13: 'D', 14 : 'E', 15 : 'F'}  
    num_final = ''
    num_convertido = []

    es_negativo = n_decimal < 0
    
    if base == 8:
        divisor = 8
        num_final = '0o'
        
    elif base==16:
        divisor = 16
        num_final = '0x'
    else:
        return ("Error con en la base de conversion, valores posibles 8 y 16")

    if es_negativo:
        cociente_num = int(-1*n_decimal)
        num_final += '-'
    else:
        cociente_num = int(n_decimal)

    # Bucle para calcular la parte entera dependiendo de la base a transformar
    while cociente_num != 0:
        cociente_num, residuo_oct = divmod(cociente_num, divisor)
        num_convertido.append(residuo_oct)

    # Se prepara la parte entera del número
    for valor in reversed(num_convertido):
        if valor >= 10:
            valor = letras_hexa[valor]
        num_final += str(valor)
       
    return num_final


n_decimal = solicitar_decimal()

print(f"Octal : {cambio_de_base(n_decimal, 8)}")
print(f"Hexa : {cambio_de_base(n_decimal, 16)}")
