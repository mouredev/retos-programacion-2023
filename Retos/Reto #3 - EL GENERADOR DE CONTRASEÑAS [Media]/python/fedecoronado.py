'''
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
'''
# tabla ascii
# minusculas --> 97 a 122
# mayusculas -->65 a 90
# numeros --> 48 a 57
# symbol --> 33 a 47 y 58 a 64 y 91 a 96 y 123 a 126
import random

while True:
    numero = int(input("cantidad de caracteres 8 a 16"))
    if numero <=16 and numero >= 8:
        break
    else:
        print("el numero debe ser netre 8 y 16. por favor reintente")
        
posibles = []
for i in range(97, 123):
    posibles.append(i)

while True:
    mayusc = input("contiene Mayusculas [y/n]")
    if mayusc == "y":
        for i in range(65, 91):
            posibles.append(i)
        break
    elif mayusc == "n":
        break
    
while True:
    numeros = input("contiene numeros [y/n]")
    if numeros == "y":
        for i in range(48, 58):
            posibles.append(i) 
        break
    elif numeros == "n":
        break
while True:       
    symbol = input("contiene symbol [y/n]")
    if symbol == "y":
        for i in range(33, 48):
            posibles.append(i)     
        for i in range(58, 65):
            posibles.append(i)
        break
    elif symbol == "n": 
        break
    
password=""
for i in range(0, numero):
    letra = random.randrange(0, len(posibles))
    password = password + chr(posibles[letra])


print(password)