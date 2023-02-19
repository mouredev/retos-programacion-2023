""" 
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

Información obtenida en: https://harrypotter.fandom.com/es/wiki/HarryPotter_Wiki
"""

import os
import random
import collections
import time

def clear_screen():
    os.system ("clear") if os.name == "posix" else os.system ("cls")

valid_options = ["1", "2", "3", "4"]

questions_list = {
    "¿Qué animal te gustaría tener como mascota?\n 1) Lechuza\n 2) Gato\n 3) Perro\n 4) Serpiente":
         (["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]),
    "¿Qué objeto mágico te gustaría tener?\n 1) La varita de sauco\n 2) La capa de invisibilidad\n 3) La piedra filosofal\n 4) El Sombrero Seleccionador":
         (["Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"]),
    "¿Qué hechizo te gustaría aprender?\n 1) Wingardium Leviosa\n 2) Expecto Patronum\n 3) Cistem aperio\n 4) Sectumsempra":
         (["Hufflepuff", "Gryffindor", "Ravenclaw", "Slytherin"]),
    "¿Qué asignatura te gustaría recibir en Hogwarts?\n 1) Artes oscuras\n 2) Teoría Mágica\n 3) Pociones\n 4) Defensa contra las artes oscuras":
         (["Slytherin", "Ravenclaw", "Hufflepuff", "Gryffindor"]),
    "¿A qué casa de Hogwarts te gustaría pertenecer?\n 1) Gryffindor\n 2) Hufflepuff\n 3) Ravenclaw\n 4) Slytherin":
         (["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"])
}

answers_list = []

questions_list_random = list(questions_list.items())
random.shuffle(questions_list_random)

for question, answers in questions_list_random:
    next_question = False

    while not next_question:
        clear_screen()
    
        print(question)

        answer = input("Selecciona una opción (1, 2, 3 o 4): ")
        if answer in valid_options:
            answers_list.append(answers[int(answer)-1])
            next_question = True
        else:
            print("\nOpcion incorrecta")
            time.sleep(1.5)

answers_counter = collections.Counter(answers_list)
house = answers_counter.most_common(1)[0][0]

print(f"\nTu casa de Hogwarts es: {house}.")
