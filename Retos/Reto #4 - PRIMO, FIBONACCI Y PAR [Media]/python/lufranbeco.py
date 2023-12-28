# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

#importamos la librería MATH para las operaciones matemáticas
import math

###################################################################################

#Creamos la función para la sucesión de fibonacci
def fibonacci(nummero_limite):# se le da como parametro una variable para el límite
    lista_fibonacci=[0, 1]# se crea la lista que almacene los números de la suceción de fibonacci
    n1=0 # la variable n1 es igual a 0
    n2=1 # la variable n2 es igual a 1
    for i in range(nummero_limite+1): # se hace un for para ir sumando n1 y n2 para ir añadiendolos a la lista
        lista_fibonacci.append(n1+n2) # se le añade el resultado de la suma a la lista
        n1=lista_fibonacci[-2] # se le asigna el penúltimo índice de la lista
        n2=lista_fibonacci[-1] # se le asigan el último índice de la lista 
    return lista_fibonacci # la función retorna la lista

###################################################################################

while True: # Hacemos un ciclo para que el usuario introduzca correctamente el número
    numero=input("Ingrese el número a validar si es primo: ") # se le pide el número
    if numero.isnumeric() == True and int(numero) >= 2: # se verifica si el número ingresado es un entero y si es mayor o igual a 2 
        break # se sale de el ciclo
    else: 
        print("¡Ingrese un número válido!") # imprime que el número no es válido

cadena_salida=f"El número {numero} " # se crea la cadena de salida
primo=False # se crea la bandera "primo"
no_primo=False # se crea la bandera "no es primo"
numero = int(numero) # se transforma la variable número a un entero
limite=math.sqrt(numero) # se crea el límite 
for i in range(2, int(limite) + 1): # se hace un for para revisar si el número es primo
    if numero % i == 0: # verifica si el residuo de el número entre la variable es igual a  0
        no_primo=True # sube la bandera "primo"
    elif numero % i != 0: # verifica si el residuo de número entre la variable es igual a 0
        primo=True # sube la bandera "no es primo"

if no_primo == True:
    cadena_salida=cadena_salida+"no es primo, "# se le añade un texto a la cadena de salida de que el número no es primo
elif primo == True:
    cadena_salida=cadena_salida+"es primo, "# se le añade un texto a la cadena de salida de que el número es primo
elif numero==2:
    cadena_salida=cadena_salida+"es primo, "# se le añade un texto a la cadena de salida de que el número es primo

##################################################################################

if numero in fibonacci(50):# si el número está en la función fibonacci entonces:
    cadena_salida=cadena_salida+"fibonacci y "# se le añade un texto a la cadena de salida de que el número es fibonacci
else:
    cadena_salida=cadena_salida+"no es fibonacci y "# se le añade un texto a la cadena de salida de que el número no es fibonacci

###################################################################################

#Verifica si el número introdusido es par

if int(numero) % 2 == 0: # si el residuo de número entre 2 es 0 entonces:
    cadena_salida=cadena_salida+"es par"# se le añade un texto a la cadena de salida de que el número es par
else:
    cadena_salida=cadena_salida+"es impar"# se le añaden un texto a la cadena de salida de que el número es impar

##################################################################################

# Imprime la salida

print(cadena_salida)