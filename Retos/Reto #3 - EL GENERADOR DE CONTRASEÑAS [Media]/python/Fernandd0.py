import random
import secrets
'''
 Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 Podrás configurar generar contraseñas con los siguientes parámetros:
 - Longitud: Entre 8 y 16.
 - Con o sin letras mayúsculas.
 - Con o sin números.
 - Con o sin símbolos.
 (Pudiendo combinar todos estos parámetros entre ellos)
'''

#Solución:
print ("Reto #3: EL GENERADOR DE CONTRASEÑAS\n")

# Variables con los parámetros designados
abecedario = "abcdefghijklmnñopqrstuvwxyz"
numeros = "0123456789"
simbolos = "<>?;'{}[]\\|!@#$%^&*()_+/-"
in_contraseña = abecedario #valor por defecto de la contraseña

#Inputs opcional de los parámetros
in_longitud = input("Para crear su contraseña, recuerde que la contraseña tiene como valores por defecto el abecedario en minuscula,\nElija la longitud [8 - 16]:  ")
in_mayusculas = input("¿Tendrá letras mayúsculas? [y/n]  ").lower()
in_numeros = input("¿Tendrá números? [y/n]  ").lower()
in_simbolos = input("Finalmente, ¿Tendrá símbolos? [y/n]  ").lower()

# En base de los inputs, agregar o no valores (mayusculas, numeros o simbolos) a la contraseña
if in_mayusculas == "y":
    in_contraseña += abecedario.upper()
else:
    in_contraseña

if in_numeros == "y":
    in_contraseña += numeros
else:
    in_contraseña

if in_simbolos == "y":
    in_contraseña += simbolos
else:
    in_contraseña

# Genera aleatoriamente la contraseña en base de los parámetros establecidos
contraseña_random = ""
for i in range(0, int(in_longitud)):
    contraseña_random += str(random.choice(in_contraseña))

# Imprime en pantalla la contrseña final
print(contraseña_random)