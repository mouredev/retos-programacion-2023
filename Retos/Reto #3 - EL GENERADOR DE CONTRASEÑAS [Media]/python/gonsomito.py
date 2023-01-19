"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
#-----------------IMPORTAMOS 
import random
import math
#----------------DEFINIMOS FUNCIONES
def comprobar_longitud(): #COMPRUEBA QUE EL TAMAÑO SEA CORRECTO Y LO DEVUELVE AL MAIN
    long_pass = 0
    while long_pass < 8 or long_pass > 16:
        long_pass = int(input("¿Qué tamaño de contraseña quieres entre 8 y 16 caracteres?"))
        if long_pass < 8 or long_pass > 16:
            print("Vuelve a intentarlo \n")
    return long_pass
    
def que_parametro(index):
    opciones=("Mayúsculas", "Números", "Símbolos")
    x=input("Quieres que contenga " + opciones[index])
    if x=="SI" or x=="si" or x=="Sí" or x=="sí" or x=="SÍ":
        return True
    else:
        return False
    
def caracteres_a_usar(mayusculas_a_usar, numeros_a_usar, simbolos_a_usar): #añade al diccionario el bloque de caracteres que se solicite
    lista_caracteres = ()
    if mayusculas_a_usar:
        lista_caracteres = lista_caracteres + ("A","B","C","D","E","F","G","H","I","J","K","L","M",
        "N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    if numeros_a_usar:
        lista_caracteres = lista_caracteres + ("0","1","2","3","4","5","6","7","8","9",)
    if simbolos_a_usar:
        lista_caracteres = lista_caracteres + (".",",",";",":","-","_","+","/","@","#","$","%","&",
            "(",")","=","?","¿","!","¡","[","]","{","}","*","ª","º")
    #print(lista_caracteres) #SOLO PARA VER SI AÑADE BIEN LOS CARACTERERS EN FUNCION DE LA ELECCIÓN
    return lista_caracteres

def password(longitud_pass, diccionrio_plus): #RECIBE EL TAMAÑO Y LA LISTA DE CARACTERES A AÑADIR
    diccionario = ("a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z") + diccionrio_plus
    tu_contrasena=""
    n=0
    while n < longitud_pass:
        tu_contrasena = tu_contrasena+diccionario[math.trunc(random.uniform(0,len(diccionario)))%len(diccionario)]
        n+=1
    print("Esta es la contraseña propuesta " + tu_contrasena)
    return tu_contrasena
    
#------EMPIEZA EL PROGRAMA
longitud = comprobar_longitud()  #PREGUNTAMOS EL TAMAÑO DE CONTRASEÑA
mayusculas = que_parametro(0)   #PREGUNTAMOS SI QUEREMOS MAYÚSCULAS
numeros = que_parametro(1)         #PREGUNTAMOS SI QUEREMOS NÚMEROS
simbolos = que_parametro(2)       #PREGUNTAMOS SI QUEREMOS SÍMBOLOS
password(longitud, caracteres_a_usar(mayusculas,numeros,simbolos)) #ENVÍO TAMAÑO Y QUÉ CARACTERES
