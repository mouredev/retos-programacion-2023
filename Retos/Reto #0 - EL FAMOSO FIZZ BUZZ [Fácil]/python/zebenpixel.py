# Reto 0: FizzBuzz
 # Escribe un programa que muestre por consola (con un print) los
 # números de 1 a 100 (ambos incluidos y con un salto de línea entre
 # cada impresión), sustituyendo los siguientes:
 # - Múltiplos de 3 por la palabra "fizz".
 # - Múltiplos de 5 por la palabra "buzz".
 # - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 #

def fizzbuzz ():
    #for
    for number in range(1, 101):
        # Si number es múltiplo de 3 y de 5, imprime "fizzbuzz"
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        # Si number es múltiplo de 3, imprime "fizz"
        elif number % 3 == 0:
            print("fizz")
        # Si number es múltiplo de 5, imprime "buzz"
        elif number % 5 == 0:
            print("buzz")
        # Si number no es múltiplo de 3 ni de 5, imprimime el número
        else:
            print(number)

fizzbuzz() 


