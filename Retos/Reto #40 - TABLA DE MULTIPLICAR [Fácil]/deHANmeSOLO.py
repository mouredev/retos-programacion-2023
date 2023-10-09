'''_______   _______  __    __       ___      .__   __. .___  ___.  _______      _______.  ______    __        ______   
.|       \ |   ____||  |  |  |     /   \     |  \ |  | |   \/   | |   ____|    /       | /  __  \  |  |      /  __  \  
.|  .--.  ||  |__   |  |__|  |    /  ^  \    |   \|  | |  \  /  | |  |__      |   (----`|  |  |  | |  |     |  |  |  | 
.|  |  |  ||   __|  |   __   |   /  /_\  \   |  . `  | |  |\/|  | |   __|      \   \    |  |  |  | |  |     |  |  |  | 
.|  '--'  ||  |____ |  |  |  |  /  _____  \  |  |\   | |  |  |  | |  |____ .----)   |   |  `--'  | |  `----.|  `--'  | 
.|_______/ |_______||__|  |__| /__/     \__\ |__| \__| |__|  |__| |_______||_______/     \______/  |_______| \______/  
.
.            _______   _______ ____    ____  _______  __        ______   .______    _______ .______      
.           |       \ |   ____|\   \  /   / |   ____||  |      /  __  \  |   _  \  |   ____||   _  \     
.           |  .--.  ||  |__    \   \/   /  |  |__   |  |     |  |  |  | |  |_)  | |  |__   |  |_)  |    
.           |  |  |  ||   __|    \      /   |   __|  |  |     |  |  |  | |   ___/  |   __|  |      /     
.           |  '--'  ||  |____    \    /    |  |____ |  `----.|  `--'  | |  |      |  |____ |  |\  \----.
.           |_______/ |_______|    \__/     |_______||_______| \______/  | _|      |_______|| _| `._____|

========================================= RESUMEN DEL PROGRAMA ========================================================

Nombre del programa: Tabla de multiplicar
Autor: Carlos
Tecnologia usada: Python
Fecha: 09/10/2023
Licencia: GNU
Descripcion: Hacer la tabla de multiplicar de un número que de el usuario.
Prerequisitos:

 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 

Notas:
Estoy en fase de aprendizaje
======================================================================================================================
'''

import os

var = os.name

def borrarPantalla():  #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

borrarPantalla() #Llamamos a la funcion anterior para invocar borrarPantalla

print("Bienbenido. Este es un programa que le mostrara la tabla de multiplicar de un número que usted elija.")
print("-----------------------------------------------------------------------------------------------------\n")
numero=int(input ("Introduzca el número:"))

for numero2 in (1,2,3,4,5,6,7,8,9,10):
    multiplicacion = numero * numero2
    
    print(("%d x %d = %d")%(numero,numero2,multiplicacion))



