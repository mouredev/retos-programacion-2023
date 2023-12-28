# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:21:27 2023

@author: oardila
"""

'''
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
'''
#Primera opción para el desarrollo
# He hecho el ejercicio para que cada vez que lo ejecutemos inicie un nuevo juego al azar entre el P1 y P2

import random

# Nombre de los jugadores
players = ["P1","P2"]

# A que equivale cada punto
points = {
    0:"Love",
    1:"15",
    2:"30",
    3:"40"
}

# Creamos los contadores de cada jugador
count_p1 = 0
count_p2 = 0

# Mientras no lleguemos al resultado deseado se ejecuta el programa
while True:
    if random.choice(players) == "P1": # selección al azar el ganador del punto
        count_p1 += 1
    else:
        count_p2 += 1
    # condiciones para ganar el partido
    if count_p1 == 4 and count_p2 < 3:
        print("Ha ganado el P1")
        break
    elif count_p2 == 4 and count_p1 < 3:
        print("Ha ganado el P2")
        break
    elif count_p1 == 3 and count_p2 == 3:
        print("Deuce")
        count = 0
        #si hay empate a 3 entonces se decide al mejor de 2 consecutivos
        while count > -2 and count < 2:
            if random.choice(players) == "P1":
                count += 1
            else:
                count -=1

            if count == 0:
                print("Deuce")
            elif count == 1:
                print("Ventaja P1")
            elif count == -1:
                print("Ventaja P2")
            elif count == 2:
                print("Ha ganado el P1")
            elif count == -2:
                print("Ha ganado el P2")
        break
    else:
        print(f'{points[count_p1]} - {points[count_p2]}')
        
 # Segunda opción para el desarrollo       
        
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
