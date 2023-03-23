'''
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
'''
for number in range(1,101):     #ciclo por contador desde 1 al 100
    if  (number %15 == 0):      # validamos si es divisible o múltiplo de 5 y 3 simultáneamente
        print("fizzbuzz\n")     
    elif (number %3 == 0):      # validamos si es divisible o múltiiplo de 3
        print("fizz\n")         
    elif  (number %5 == 0):     # validamos si es divisible o múltiiplo de 5
        print("buzz\n")   
    else:                       # validamos si no es divisible o múltiplo de 5 ni 3
        print(number,"\n") 