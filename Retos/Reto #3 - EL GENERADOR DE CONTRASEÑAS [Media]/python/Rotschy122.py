'''
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
 - Longitud: Entre 8 y 16.
 - Con o sin letras mayúsculas.
 - Con o sin números.
 - Con o sin símbolos.
 (Pudiendo combinar todos estos parámetros entre ellos)
'''

import string
import random


def generar_contraseña(longitud: int, con_letras_mayusculas: bool = False, con_numeros: bool = False, con_simbolos: bool= False):
    if longitud < 8 or longitud > 16: return 'Longitud solicitada erronea'
    lista_caracteres_habilitados = []
    lista_caracteres_habilitados = obtener_lista_con_caracteres_habilitados(con_letras_mayusculas, con_numeros, con_simbolos )
    contraseña = ''  

    for i in range(longitud):
        caracter_aleatorio = random.choice(lista_caracteres_habilitados)
        contraseña = contraseña + caracter_aleatorio
    return contraseña

def obtener_lista_con_caracteres_habilitados(con_letras_mayusculas: bool = False, con_numeros: bool = False, con_simbolos: bool= False):
    lista_caracteres_habilitados = []
    for caracter in string.ascii_lowercase: lista_caracteres_habilitados.append(caracter)
    if con_letras_mayusculas: 
        for caracter in string.ascii_uppercase: lista_caracteres_habilitados.append(caracter)
    if con_numeros:
        for caracter in string.digits: lista_caracteres_habilitados.append(caracter)
    if con_simbolos:
        for caracter in string.punctuation: lista_caracteres_habilitados.append(caracter)
    return lista_caracteres_habilitados


'''Pruebas'''
print("Contraseñas aleatorias que permiten mayúsculas, números y símbolos")
for pass_length in range(6, 20):
    print(generar_contraseña(pass_length, True, True, True))
    
# print("Contraseñas aleatorias que permiten mayúsculas y números, pero NO símbolos")
# for pass_length in range(8, 16):
#     print(generar_contraseña(pass_length, True, True, False))
    
# print("Contraseñas aleatorias que permiten mayúsculas, pero NO números ni símbolos")
# for pass_length in range(8, 16):
#     print(generar_contraseña(pass_length, True, False, False))
    
# print("Contraseñas aleatorias que NO permiten mayúsculas ni números ni símbolos")
# for pass_length in range(8, 16):
#     print(generar_contraseña(pass_length, False, False, False))
