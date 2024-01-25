# Create by luiveldel
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

num_1_100 = range(1, 101)

for n in num_1_100:
    if n % 3 == 0:
        print("fizz",'\n')
    elif n % 5 == 0:
        print("buzz",'\n')
    elif n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz",'\n')
    else:
        print(n,'\n')