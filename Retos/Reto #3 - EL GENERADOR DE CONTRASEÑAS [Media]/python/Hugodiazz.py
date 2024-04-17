 # Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 # Podrás configurar generar contraseñas con los siguientes parámetros:
 # - Longitud: Entre 8 y 16.
 # - Con o sin letras mayúsculas.
 # - Con o sin números.
 # - Con o sin símbolos.
 # (Pudiendo combinar todos estos parámetros entre ellos)

import random
def generadorContrasena(longitud: int, mayus: bool, num: bool, simb: bool):
    #Sistema ASCII
    simbolos1 = list(range(32, 48))
    simbolos2 = list(range(58, 65))
    simbolos = simbolos1 + simbolos2

    numeros = list(range(48, 58))
    mayusculas = list(range(65, 91))
    minusculas = list(range(97, 123))

    caracteres_disponibles= []

    if longitud >= 8 and longitud <= 16:
        caracteres_disponibles = agregarLista(caracteres_disponibles, minusculas)

        if mayus:
            caracteres_disponibles = agregarLista(caracteres_disponibles, mayusculas)
        if num:
            caracteres_disponibles = agregarLista(caracteres_disponibles, numeros)
        if simb:
            caracteres_disponibles = agregarLista(caracteres_disponibles, simbolos)
        
        return crearContrasena(longitud, caracteres_disponibles)
    else:
        return ('La contraseña debe tener entre 8 y 16 caracteres')

def crearContrasena(longitud, caracteres):
    contrasena = ''
    contador = 0
    while contador < longitud:
        caracterSeleccionado = random.choice(caracteres)
        contrasena += caracterSeleccionado
        contador += 1
    
    return contrasena
    
def agregarLista(lista, lista2):
    for elemento in lista2:
        lista.append(chr(elemento))
    return lista
    

print('Tu contraseña es: ' + generadorContrasena(8, True, False, False))
print('Tu contraseña es: ' + generadorContrasena(9, False, True, False))
print('Tu contraseña es: ' + generadorContrasena(10, False, False, True))

print('Tu contraseña es: ' + generadorContrasena(11, True, True, False))
print('Tu contraseña es: ' + generadorContrasena(12, False, True, True))
print('Tu contraseña es: ' + generadorContrasena(13, True, False, True))

print('Tu contraseña es: ' + generadorContrasena(14, True, True, True))
print('Tu contraseña es: ' + generadorContrasena(15, False, False, False))

print('Tu contraseña es: ' + generadorContrasena(7, True, False, False))
print('Tu contraseña es: ' + generadorContrasena(17, True, False, False))
