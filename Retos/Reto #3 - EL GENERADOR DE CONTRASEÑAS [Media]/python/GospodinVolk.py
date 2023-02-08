'''
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
'''
import random
import string

# función que elige un elemento aleatorio dentro de una lista
def genera_caracter(lista):
    car = str(random.choice(lista))
    return car

# listas de elementos
lista_nums = range(10)
lista_mays = list(string.ascii_uppercase)
lista_mins = list(string.ascii_lowercase)
lista_symb = list(map(chr, range(33, 47))) + list(map(chr, range(58, 65)))

# variable que contendrá la contraseña
password = ''

# pedimos las características del número y hacemos una lista con las listas de los elementos que vamos a usar. Las minúsculas siempre están
lista =[lista_mins]

respuesta = input("¿Lleva mayúsculas (s/n)? ").lower()
if respuesta == 's':
    lista.append(lista_mays)

respuesta = input("¿Lleva números (s/n)? ").lower()
if respuesta == 's':
    lista.append(lista_nums)

respuesta = input("¿Lleva símbolos (s/n)? ").lower()
if respuesta == 's':
    lista.append(lista_symb)



# pedimos el número de caracteres
num_car = 0


while num_car < 8 or num_car > 16:
    num_car = int(input("Dime el número de caracteres del password (entre 8 y 16 > "))



# bucle: para cada carácter de la contraseña elegimos una lista aleatoria dentro de la lista y un carácter dentro de ella
for i in range(num_car):
    temp_list = random.choice(lista)
    car = random.choice(temp_list)
    password = password + str(car)

print("La contraseña es: " + password)






