# /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

#Variables a utilizar 
num_max = 100
num_min = 1

#Ciclo de busqueda
for i in range(num_min,num_max + 1):

    #Condicionales
    #Si el numero es multiplo de 3 y 5
    if (i % 3 == 0 and i % 5 == 0):
        print("fizzbuzz \n")
    #Si el numero es multiplo de 3
    elif (i % 3 == 0):
        print("fizz \n")
    #Si el numero es multiplo de 5
    elif (i % 5 == 0):
        print("buzz \n")
    #Si el numero no cumple ninguna condicion se imprime directamente
    else:
        print(i, '\n')