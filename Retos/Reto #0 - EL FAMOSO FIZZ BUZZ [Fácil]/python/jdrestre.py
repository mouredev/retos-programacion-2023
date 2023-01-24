# Reto #0: EL FAMOSO "FIZZ BUZZ"
# Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23

# Enunciado

# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


""" Código Solución """

# El código siguiente está imprimiendo los números del 1 al 100, pero si el número es divisible por 3,
# imprime "fizz", si el número es divisible por 5, imprime "buzz", y si el número es
# divisible por ambos 3 y 5, imprime "fizzbuzz".
for i in range(1, 101, 1):
    if i%5 == 0 and i%3 == 0:
      print("fizzbuzz")
    elif i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(i)
