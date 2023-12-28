import random

letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_mayusculas=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros=["1","2","3","4","5","6","7","8","9","0"]
simbolos=["|","°","!","#","$","%","&","/","(",")","=","?","¡","¿","{","}","[","]","+","*","_","@",":","-"]
contraseña=[]
cantidadnumeros=0
cantidadsimbol=0
cantidadmayusculas=0
password=""

print("\t GENERADOR DE CONTRASEÑAS")
longitud=int(input("Digita la longitud de tu contraseña (min 8, max 16): "))
if longitud<8 or longitud>16:
    print("ingrese una longitud entre 8 y 16")
    
else:
    mayusculas=input("Quieres emplear mayusculas? Y/N: ")
    if mayusculas.upper()=="Y":
        cantidadmayusculas=(longitud//3)
    elif mayusculas.upper()=="N":
        cantidadmayusculas=0
    else:
        print("opcion invalida, se tomara como No")

    num=input("Quieres emplear numeros) Y/N: ")

    if num.upper()=="Y":
        cantidadnumeros=(longitud//3)
    elif num.upper()=="N":
        cantidadnumeros=0
    else:
         print("opcion invalida, se tomara como No")


    simbol=input("Quieres emplear simbolos? Y/N: ")
    if simbol.upper()=="Y":
        cantidadsimbol=(longitud//3)
    elif simbol.upper()=="N":
        cantidadsimbol=0
    else:
         print("opcion invalida, se tomara como No")

    cantidadletras=longitud-cantidadnumeros-cantidadsimbol-cantidadmayusculas
        
    contraseña+=random.sample(letras_mayusculas,cantidadmayusculas) #se agregan las mayusculas de manera aleatoria
    
    contraseña+=random.sample(letras,cantidadletras) #se agregan las minusculas de manera aleatoria
    
    contraseña+=random.sample(numeros,cantidadnumeros) #se agregan los numeros de manera aleatoria
    
    contraseña+=random.sample(simbolos,cantidadsimbol) #se agregan los simbolos de manera aleatoria

    contraseña=random.sample(contraseña,len(contraseña))#se genera la contraseña en orden aleatorio

    for each in contraseña:
        password+=each
    print(f"Tu contraseña es: \n {password}")