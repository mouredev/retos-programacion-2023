"""
 Crea una función que reciba dos cadenas de texto casi iguales, a excepción de uno o varios caracteres. 
 La función debe encontrarlos y retornarlos en formato lista/array.
 - Ambas cadenas de texto deben ser iguales en longitud.
 - Las cadenas de texto son iguales elemento a elemento.
 - No se pueden utilizar operaciones propias del lenguaje que lo resuelvan directamente.
 
 Ejemplos:Reto #29 - EL CARÁCTER INFILTRADO
 - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
"""

def compara_cadena(cadena1, cadena2):
    #iniciamos variables: i para movernos por el array/string lista_diferencias para almacenar diferecias
    i=0
    lista_diferencias=[]
    #compara tamaños por si no fueran iguales. Si no coincide nos vamos.
    if len(cadena1) != len(cadena2):
        return "El tamaño es incorrecto"
    #recorrer ambas cadenas con el mismo index y comprobar cada carácter.
    while i<len(cadena1):
        if cadena1[i] != cadena2[i]:
            lista_diferencias.append(cadena2[i])
        i=i+1
    return lista_diferencias
    
#ejemplos
cadena_uno="Me llamo mouredev"
cadena_dos="Me llemo mouredov"
print(compara_cadena(cadena_uno,cadena_dos))

cadena_uno="Se llama.Brais Moure"
cadena_dos="Se llama brais moure"
print(compara_cadena(cadena_uno,cadena_dos))

cadena_uno="A lo loco lo colocó Lola"
cadena_dos="A la loca le coloca lalo"
print(compara_cadena(cadena_uno,cadena_dos))

cadena_uno="Me llamo mouredev"
cadena_dos="Me llemo gonsomito"
print(compara_cadena(cadena_uno,cadena_dos))

cadena_uno="Me llamo moure.dev"
cadena_dos="Me llamo gonsomito"
print(compara_cadena(cadena_uno,cadena_dos))

cadena_uno="Me llamo"
cadena_dos="Me llamo"
print(compara_cadena(cadena_uno,cadena_dos))
