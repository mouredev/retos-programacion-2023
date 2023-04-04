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


n_decimal = solicitar_decimal()

# Verifica si el número ingresado es negativo y asigna True a la variable es_negativo en caso de ser verdadero
es_negativo = n_decimal < 0

# Inicializa la lista octal
octal_entero = []
octal_decimal = []
decimal_octal=0

if es_negativo:
    # Si el número es negativo, cambia el signo a positivo y agrega un prefijo de '0o-' al número octal resultante
    cociente_oct = int(-1*n_decimal)
    num_octal = '0o-'
    decimal_octal = -1*(n_decimal+cociente_oct)
    print(decimal_octal)
else:
    # Si el número es positivo, utiliza el mismo valor para el cociente y agrega un prefijo de '0o' al número octal resultante
    cociente_oct = int(n_decimal)
    num_octal = '0o'
    decimal_octal = n_decimal-cociente_oct

num_octal_dec =''

print(decimal_octal)


# Convierte el número decimal a octal utilizando el algoritmo de división por 8
while cociente_oct != 0:
    cociente_oct, residuo_oct = divmod(cociente_oct, 8)
    octal_entero.append(residuo_oct)

# Concatena los valores de la lista octal, en orden inverso, al número octal resultante
for valor in reversed(octal_entero):
    num_octal += str(valor)

print (f"Parte entera {num_octal}")

if decimal_octal !=0 :    
    entero_oct = decimal_octal
    contador = 0

    while entero_oct != 0 and contador<=5 :
        entero_oct = entero_oct * 8
        octal_decimal.append(int(entero_oct))
        entero_oct= entero_oct % 1
        contador +=1
    octal_final=num_octal+'.'+ ''.join(str(x) for x in octal_decimal)
else:
    octal_final=num_octal

print(f"Numero final en octal {octal_final}")

