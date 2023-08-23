# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 21:26:55 2023

@author: Jarko
"""

# Reto MoureDev cifrado Cesar

# Funcion cifrado

def cifrado(texto,k, opcion):
    
    # creamos la variable string cifrado.

    cifrado = ""
    

    # Bucle para cada letra del texto
    
    for letra in texto:

        if letra == letra.lower () : 
        
            alfabeto = "abcdefghijklmnñopqrstuvwxyz"
            
            if opcion == 2: # En caso de descifrar lo hacemos al reves
                
                alfabeto = alfabeto[::-1]
            
            letra_cifrada = alfabeto[(alfabeto.index(letra) + k) % len(alfabeto)]
            
            cifrado += letra_cifrada
            
            
        
        elif letra == letra.upper () :
        
            alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
                     
            if opcion == 2:
                    
                alfabeto = alfabeto[::-1]
            
            cifrado += alfabeto [(alfabeto.index(letra) + k) % len(alfabeto)]
        
        else: # En caso de usar simbolos o numeros se mantienen igual
            
            cifrado += letra
    
     
    # Cargamos la clave cifrada/descifrada en salida
    
    print ("Hasta pronto")
    return (cifrado)


# Funcion menu para cifrar o descifrar

def menu():
    
    print ("¿Que quieres hacer?")
    print ()
    print ("1. Cifrado")
    print ("2. Descifrado")
    print ("3. Salir")
    print ()

    opcion = input ( "Selecciona una opción: ")
    opcion = int (opcion)

    if opcion == 1: # Hacemos cifrado

        texto = input ("Introduce el texto a cifrar:  ")
    
        k = int (input ("Introduce el valor de desplazamiento: "))
    
        texto_cifrado = cifrado(texto, k, opcion)
        
        print ()
        print ("El texto cifrado es: ", texto_cifrado)
        print ()
        
        menu ()
    
    elif opcion == 2: # Hacemos descifrado

        texto = input ("Introduce el texto a descifrar: ")
        k = int (input ("Introduce el valor de desplazamiento: "))
        
        
        texto_descifrado = cifrado (texto, k, opcion)
        print ()
        print ("El texto descifrado es: ", texto_descifrado)
        print ()
        
        menu ()
    
    elif opcion == 3: # Cerramos el programa

        return

    
    else:
    
        print ("Introduce una opción posible, 1, 2 o 3")
        menu ()

    
menu()
