"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

 
def print_fixx_buzz():

    cadena = ""
    
    for i in range(100):
        if  ((i+1)%3 == 0) and ((i+1)%5 == 0):
            cadena="fizzbuzz"
        elif ((i+1)%3 == 0) : 
           cadena="fizz" 
        elif  ((i+1)%5 == 0) :
            cadena="buzz"
        
            
        else :
            cadena=i+1
            
        print(cadena)



print_fixx_buzz()
