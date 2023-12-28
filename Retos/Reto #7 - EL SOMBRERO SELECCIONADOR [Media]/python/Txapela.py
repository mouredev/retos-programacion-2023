#!/usr/bin/env python

'''
 Crea un programa que simule el comportamiento del sombrero seleccionador del
 universo mágico de Harry Potter.
 - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 - Cada pregunta tendrá 4 respuestas posibles (también a seleccionar una a través de la terminal).
 - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 - Por ejemplo, en Slytherin se premia la ambición y la astucia.
'''

# Casas de Hogwarts
casas = {"a":"Gryffindor", "b":"Hufflepuff", "c":"Ravenclaw", "d":"Slytherin"}
 
# Puntuaciones
a,b,c,d = 0,0,0,0

# Preguntas y respuestas
preguntas ={
    "¿Cuál es tu color favorito?: \n A - Rojo \n B - Amarillo \n C - Azul \n D - Verde",

    "¿Cuál es tu asignatura favorita?: \n A - Defensa contra las Artes Oscuras \n B - Herbología \n C - Adivinación \n D - Pociones",
    
    "¿Qué cualidad valoras más en ti mismo? \n A - Valentía \n B - Lealtad \n C - Inteligencia \n D - Ambición",
    
    "¿Cuál es tu animal favorito? \n A - León \n B - Tejón \n C - Águila \n D - Serpiente",

    "Escoge uno de estos elementos: \n A - Tierra \n B - Fuego \n C - Aire \n D - Agua",
}


#Presentación
print ("~~~~~~~~~~~~~~~~~~~~~~~~~")
print (" El sombrero de Hogwarts")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~")
while not False:
    r = (input("Preparado para el test??? ('S' o 'N')")).lower()
    if r == "s":
        print ("\nAdelante!!!\n")
        break
    elif r == "n":
        print ("\nCobardeeeeeee!!!\n")
        exit()
    elif r != "s" and r !="n":
        print ("\nOpción escogida NO valida...\n")

# Preguntamos      
for i in preguntas:
    print (i)
    respuesta = input("Escoge una opción:\n").lower()
    if respuesta == "a":
        a +=1
    elif respuesta == "b":
        b +=1
    elif respuesta == "c":
        c +=1
    elif respuesta == "d":
        d +=1
    else:
        print ("Opción escogida NO valida...")
        break

#Presentamos resultados       
if a>b and a>c and a>d:
    print ("Perteneces a la casa de Gryffindor")
elif b>c and b>d:
    print ("Perteneces a la casa de Hufflepuff")
elif c>d:
    print ("Perteneces a la casa de Ravenclaw")
else:
    print ("Perteneces a la casa de Slytherin")
