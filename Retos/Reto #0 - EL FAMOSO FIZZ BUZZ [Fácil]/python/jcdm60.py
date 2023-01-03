#
# Reto #0: EL FAMOSO "FIZZ BUZZ"
#
# Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23
#
# Enunciado
#
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#

for i in range(1,101):
    fizz = 'Fizz' if i%3==0 else ''
    buzz = 'Buzz' if i%5==0 else ''
    print(f'{fizz}{buzz}' or i)
