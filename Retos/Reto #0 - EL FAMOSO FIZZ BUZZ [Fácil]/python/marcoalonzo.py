'''
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
'''

#Function creation
def fizzbuzz():
    #loop through 1-100
    for num in range(1,101): 
        #if the number is divisable by 3 and 5, we print "fizzbuzz"
        if (num % 3 == 0 and num % 5 == 0): 
            print("fizzbuzz")
        #if the number is divisable by 3, we print "fizz"
        elif num % 3 == 0:
            print("fizz")
        #if the number is divisible by 5, we print "buzz"
        elif num % 5 == 0:
            print("buzz")
        else:
        #if the number is not divisable by 3 or 5, we just print the number
            print(num)

#We invoke the created function
fizzbuzz()