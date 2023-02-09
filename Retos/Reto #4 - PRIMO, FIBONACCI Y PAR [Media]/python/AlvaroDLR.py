'''
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''
import math

result = ""
def es_primo(n):
    global result
    result = "es primo, "
    for i in range(2,n):
        if (n%i) == 0:
            #return True
            result = "no es primo, "
            
def is_square(x):
	s = int(math.sqrt(x))
	return s*s == x

# Returns true if n is a Fibinacci Number, else false
def is_fibonacci(n):
    global result
    if is_square(5*n*n + 4) or is_square(5*n*n - 4) == True:
        result += "fibonacci, "
    else:
        result += "no es fibonacci, "

def es_par(n):
    global result
    if n%2 == 0:
        #return True
        result += "y es par."
    else:
        #return False
        result += "y es impar."

try:
    number = int(input("Escriba un numero entero: "))
    es_primo(number)
    is_fibonacci(number)
    es_par(number)
    print(f"{number} {result}")
except ValueError:
    print("No se admiten numero decimales")