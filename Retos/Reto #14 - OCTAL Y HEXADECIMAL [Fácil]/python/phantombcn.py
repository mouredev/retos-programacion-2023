while True:
    try:
        # Solicita al usuario que ingrese un número decimal y lo convierte a entero
        n_decimal = float(input("Introduce un número en decimal: "))
        break
    except ValueError:
        # Si se ingresa un valor no numérico, muestra un mensaje de error en la pantalla y solicita al usuario que ingrese un número válido
        print("Debe introducir un número")

# Verifica si el número ingresado es negativo y asigna True a la variable es_negativo en caso de ser verdadero
es_negativo = False
if n_decimal < 0:
    es_negativo=True

# Inicializa la lista octal
octal_entero = []
octal_decimal = []

if es_negativo:
    # Si el número es negativo, cambia el signo a positivo y agrega un prefijo de '0o-' al número octal resultante
    cociente_oct = int(-1*n_decimal)
    num_octal = '0o-'
    decimal_octal = round(n_decimal+cociente_oct,5)    
else:
    # Si el número es positivo, utiliza el mismo valor para el cociente y agrega un prefijo de '0o' al número octal resultante
    cociente_oct = int(n_decimal)
    num_octal = '0o'
    decimal_octal = round(n_decimal-cociente_oct,5)


print(decimal_octal)


# Convierte el número decimal a octal utilizando el algoritmo de división por 8
while cociente_oct != 0:
    cociente_oct, residuo_oct = divmod(cociente_oct, 8)
    octal_entero.append(residuo_oct)

# Concatena los valores de la lista octal, en orden inverso, al número octal resultante
for valor in reversed(octal_entero):
    num_octal += str(valor)

# Imprime el número octal resultante en la pantalla
print (num_octal)
