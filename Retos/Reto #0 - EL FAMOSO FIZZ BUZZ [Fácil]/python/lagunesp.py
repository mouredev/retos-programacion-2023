#2023.01.08
#lagunesp
'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 
'''

def fizz_buzz(x):
    resp = ""
    if(x % 3):
        resp = "fizz"
    if(x % 5):
        resp = resp + "buzz"
    return resp

for i in range(101):
    print(f"{i} :  {fizz_buzz(i)}")
    
