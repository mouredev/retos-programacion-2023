# Define una función para solicitar un número decimal al usuario y asegurarse de que sea válido
def solicitar_decimal():
    while True:
        try:
            # Solicita al usuario que ingrese un número decimal y lo convierte a entero
            n_decimal = float(input("Introduce un número en decimal: "))
            return n_decimal
        except ValueError:
            # Si se ingresa un valor no numérico, muestra un mensaje de error en la pantalla y solicita al usuario que ingrese un número válido
            print("Debe introducir un número")

def cambio_de_base (n_decimal, base):

    # Verifica si el número ingresado es negativo y asigna True a la variable es_negativo en caso de ser verdadero
    letras_hexa = {10 : 'A', 11 : 'B', 12 : 'C', 13: 'D', 14 : 'E', 15 : 'F'}
    
    if base == 8:
        divisor = 8
        num_octal = '0o'
        
    elif base==16:
        divisor = 16
        num_octal = '0h'
    else:
        return (-1)
    
    es_negativo = n_decimal < 0

    # Inicializa la lista octal
    octal_entero = []
    octal_decimal = []
    decimal_octal=0

    if es_negativo:
        # Si el número es negativo, cambia el signo a positivo y agrega un prefijo de '0o-' al número octal resultante
        cociente_oct = int(-1*n_decimal)
        num_octal += '-'
        decimal_octal = -1*(n_decimal+cociente_oct)
        print(decimal_octal)
    else:
        # Si el número es positivo, utiliza el mismo valor para el cociente y agrega un prefijo de '0o' al número octal resultante
        cociente_oct = int(n_decimal)
        decimal_octal = n_decimal-cociente_oct

    # Bucle para calcular la parte entera dependiendo de la base a transformar
    while cociente_oct != 0:
        cociente_oct, residuo_oct = divmod(cociente_oct, divisor)
        octal_entero.append(residuo_oct)

    # Se prepara la parte entera del número
    for valor in reversed(octal_entero):
        if valor >= 10:
            valor = letras_hexa[valor]
        num_octal += str(valor)

    print (f"Parte entera {num_octal}")

    if decimal_octal !=0 :    
        entero_oct = decimal_octal
        contador = 0

        while entero_oct != 0 and contador<=5 :
            entero_oct = entero_oct * divisor
            if entero_oct >= 10:
                octal_decimal.append(letras_hexa[int(entero_oct)])
            else:
                octal_decimal.append(int(entero_oct))
            entero_oct= entero_oct % 1
            contador +=1
        octal_final=num_octal+'.'+ ''.join(str(x) for x in octal_decimal)
    else:
        octal_final=num_octal
        
    return octal_final




n_decimal = solicitar_decimal()

print(f"Octal : {cambio_de_base(n_decimal, 8)}")
print(f"Hexa : {cambio_de_base(n_decimal, 16)}")


