#  */
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */

def run():
    
    def comprobar_numero(numero):
        
        print("El numero",numero)

        #Primo
        if numero == 2 or numero == 3 or numero == 5 or numero ==7:
            print("Es primo")
        elif numero == 1 or numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
            print("No es primo")
        else:
            print("Es primo")

        #fibonacci
        var1 = 0
        var2 = 1
        list = [var1]    

        for x in range(50):      
            fib = var1 + var2
            var2 = var1
            var1 = fib
            list.append(fib)

        if numero in list:
            print("Es fibonacci")
        else:
            print("No es fibonacci")
            
        #pan
        if numero % 2 == 0:
            print("Es par")
        else:
            print("Es impar")

    comprobar_numero(2)
    comprobar_numero(7)

if __name__ == "__main__":
    run()