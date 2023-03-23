"""
    * Escribe un programa que muestre por consola (con un print) los
    * números de 1 a 100 (ambos incluidos y con un salto de línea entre
    * cada impresión), sustituyendo los siguientes:
    * - Múltiplos de 3 por la palabra "fizz".
    * - Múltiplos de 5 por la palabra "buzz".
    * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
    
"""
def main():
    #funcion lambda para saber si un numero es multiplo de x
    multiplo = lambda number,multiplo : number % multiplo == 0
    
    for i in range(1,101,1):
        #si el numero actual es multiplo de 3 y 5 se imprime fizzbuzz
        if multiplo(i,3) and multiplo(i,5):
            print("fizzbuzz")
        #si el numero actual es multiplo de 3 se imprime fizz
        elif multiplo(i,3):
            print("fizz")
        #si el numero actual es multiplo de 5 se imprime buzz
        elif multiplo(i,5):
            print("buzz")
        #si no hay multiplos de 3 ni de 5 se imprime el numero
        else:
            print(i)

if __name__ == "__main__": 
		main() 
