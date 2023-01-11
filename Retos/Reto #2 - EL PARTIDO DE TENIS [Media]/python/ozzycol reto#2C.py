# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:28:36 2023

@author: oardila
"""

import random

# Nombre de los jugadores
players = ["P1","P2"]

# funcion que realiza la converción de los puntos a nomenclatura
def convert_points(points):
    if points == 0:
        return "Love"
    elif points == 1:
        return "15"
    elif points == 2:
        return "30"
    elif points == 3:
        return "40"
#Se defiene 2 variables para los puntos de cada jugador
p1 = 0
p2 = 0
# Entra en un loop
while True:
    #Se solicita ingresar el punto para quien va, se convierte a mayusculas
    p = random.choice(players)

    if p == "P1": #si el usuario digita P1 aumenta punto en 1
        p1 += 1
    elif p == "P2": #si el usuario digita P2 aumenta punto en 1
        p2 += 1
    else: # si el usuario digita un valor diferente a p1 o p2 imprime mensaje y los contadores se mantienen
        print("El jugador introducido no es valido, el juego sigue: ")

    if p1 == 3 and p2 == 3:
        print("Deuce") #si p1 y p2 son 3 el resultado es deuce
    elif p1 <= 3 and p2 <= 3: # si ambos tienen menos de 3 llama funcion y pinta el resultado
        print(convert_points(p1) + " - " + convert_points(p2))
    else:
        if p1 - 1 == p2:
            print("Ventaja para el jugador P1")
        elif p2 - 1 == p1:
            print("Ventaja para el jugador P2")
        else:
            if p1 > p2:
                print("El jugador P1 ha ganado")
                break
            elif p2 > p1:
                print("El jugador p2 ha ganado");
                break
            else:
                print("Deuce");
