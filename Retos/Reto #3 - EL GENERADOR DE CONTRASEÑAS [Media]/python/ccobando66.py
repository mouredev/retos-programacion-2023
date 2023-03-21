#Reto 3 generador de contraseñas 

"""
se importa las librerias nativas de python para trabajar con string

 - digit : valores numerico
 - punctuation: caracteres especiales
 - ascii_letters: caracteres entre mayúsculas y minúsculas 
 - ascii_lowercase: solo minúsculas
 
para trabajar valores alieatorios, se usa choice, es una funcion
que permite elegir valores aleatorios de una lista o tupla
"""

from string import (
    digits,ascii_lowercase,ascii_letters,
    punctuation
)
from random import choice

#almacena valoes obtenidos desde la funcion choice
txt = []

#opciones de accesos para llamar desde una llave, las funciones de string
my_options = {
    1: ascii_lowercase,
    2: ascii_letters,
    3: digits,
    4: punctuation
}

"""
En este caso, almacena el valor de largo de caracteres, uno de los inconvenientes 
es que el usuario ingrese valores negativos para solucionar se resuelve de la siguiente manera:
  - abs valor absoluto recibe numeros negativos, a positivo 
en otros lenguajes de programación seria uint,los valores de tipo uint acepta solo valores positivos 
"""
largo = abs(int(input("Escribe el largo de la contraseña a generar: ")))

#validador de largo a generar acepta valores mayores a 8 y menores a 16
while largo < 8 or largo > 16 :
    largo = abs(int(input("Error! El largo es menor a 8 o excede más de 16 caracteres: ")))
    
    
#lista de opciones muestra al usuario en pantalla
ops = abs(int(input(f"!-------- Opciones para generar contraseña  -------------!\n"
                    f"! 1. Solo letras minusculas                              !\n"
                    f"! 2. Combinación entre mayúsculas y minúsculas           !\n"
                    f"! 3. Combinación entre mayúsculas , minúsculas y Numeros !\n"
                    f"! 4. Todas las Combinaciones                             !\n"
                    f"! -------------------------------------------------------!\n"
                    f"ops: "
                    )))

#validador de opciones acepta valores en el rango de 1-4
while ops == 0 or ops > 4:
    ops = abs(int(input("Error! opcion no valida rango aceptado es de 1 a 4: ")))
    

#funcion generadora de contraseña recibe 2 int y devuelve un None
def generate_passwd(largo:int, ops: int)->None:
    """
     se compara el lago de la lista con el valor del usuario
     si el valor es menor o igual al largo restandole 1 porque 
     el ciclo while imprima el ultimo caracter generado. 
    """
    while len(txt) <= (largo-1) :
        #valida si a opcion ingresada son valores menores a 3 = 1 y 2 el 3 no lo entiene en cuenta
        if ops<3:
            txt.append(choice(my_options.get(ops)))
        else:
            #elige el valor aleatorio y lo guarde en my_change
            my_change = choice(range(1,ops+1))
            #elige el valor aleatorio desde la clave que contiene funcion asociada buscando
            #desde el valor generado de my_change
            txt.append(choice(my_options.get(my_change)))
               
         
#match es equivalente a switch en otros lenguajes esta disponibe desde la
#version 3.10 de python         
match ops:
    case 1:
          generate_passwd(largo=largo,ops=ops)
    case 2:
          generate_passwd(largo=largo,ops=ops)
    case 3:
          generate_passwd(largo=largo,ops=ops)
    case 4:
          generate_passwd(largo=largo,ops=ops)
             

#muestra en pantalla la contraseña generada
print(f"contraseña generada: {''.join(map(str,txt))}")
