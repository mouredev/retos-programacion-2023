### Reto #0: EL FAMOSO "FIZZ BUZZ"
#### Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23

# * Escribe un programa que muestre por consola (con un print) los
# * números de 1 a 100 (ambos incluidos y con un salto de línea entre
# * cada impresión), sustituyendo los siguientes:
# * - Múltiplos de 3 por la palabra "fizz".
# * - Múltiplos de 5 por la palabra "buzz".
# * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
# */

#Rango:
NUMERO_INICIAL=1
NUMERO_FINAL=100

for i in range(NUMERO_INICIAL, NUMERO_FINAL+1,1):
    MUL3=i%3
    MUL5=i%5

    if MUL3==0:
        if MUL5==0:
            print("fizzbuzz")
        else:
            print("fizz")
    else:
        if MUL5==0:
            print("buzz")
        else:
            print(i)