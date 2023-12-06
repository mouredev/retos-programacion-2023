"""
#  Crea un programa que simule el comportamiento del sombrero selccionador del
#  Universo mágico de Harry Potter.
#  - De ser posible realizará 5 preguntas(como mínimo) a través de la terminal.
#  - Cada pregunta tendrá 4 respuestas posibles(también a selecciona una a través de terminal).
#  - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#    coloque al alumno en una de las 4 casas de Hogwarts(Gryffindor, Slytherin, Hufflepuff y Ravenclaw)
#  - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#    Por ejemplo, en Slytherin se premia la ambición y la astucia.
"""

import random
import os
import numpy as np


def sorting_hat():
    os.system("cls")
    print("\n")
    print("\n")
    Gryffindor = 0
    Hufflepuff = 0
    Ravenclaw = 0
    Slytherin = 0
    questions = {
        "> ¿Cuál de las siguientes odiarías más que la gente te llamara?": {
            "Cobarde": 1, "Egoista": 2, "Ignorante": 3, "Ingenuo": 4
        },
        "> ¿Cómo le gustaría ser conocido en la historia?": {"El gran": 1, "El bueno": 2, "El sabio": 3, "El audaz": 4},
        "> ¿Qué tipo de instrumento agrada mas a tu oído?": {"Trompeta": 1, "Tambores": 2, "Violin": 3, "Piano": 4},
        "> ¿Qué es lo que más anhelas aprender en Hogwarts?": {
            "Volar en una escoba": 1, "Todo sobre criaturas mágicas, hacerse amigo y protegerlos": 2, "Cada área de magia que pueda": 3, "Maleficios y hechizos": 4},
        "> Tú y dos amigos deben cruzar un puente custodiado por un troll de río que insiste en\n luchar contra uno de ustedes antes de que los deje pasar a todos. Tú:": {
            "Te ofreces como voluntario": 1, "¿Sugieres que los tres deben luchar? (sin decírselo al troll)": 2, "¿Intentas confundir al troll para que te deje pasar a los tres sin luchar?": 3, "¿Sugerir un sorteo para decidir quién de ustedes peleará?": 4},
        "> A altas horas de la noche, caminando solo por la calle, escuchas un grito peculiar\n que crees que tiene una fuente mágica. ¿Cuál elegirías?:": {
            "Tomas tu varita y tratas de descubrir la fuente del ruido?": 1, "Retirarse a las sombras para esperar los acontecimientos, mientras revisas los hechizos defensivos y ofensivos más apropiados": 2, "¿Proceder con precaución, manteniendo una mano en tu varita oculta y atento a cualquier perturbación?": 3, "¿Tomar tu varita y mantenerte firme?": 4},
    }
    # Guarda las questions en una lista
    all_questions = list(questions.items())
    # print(all_questions)
    # print(len(questions))

    for i in range(5):  # ULTIMO CAMBIO REVISAR
        os.system("cls")
        random_question = random.choice(all_questions)
        print("SOMBRERO SELECCIONADOR: \n")
        print(random_question[0])
        n1, n2, n3, n4 = random_question[1].values()
        # print(options)
        a, b, c, d = random_question[1].keys()
        print(f"""    {n1}) {a}\n    {n2}) {b}\n    {n3}) {c}\n    {n4}) {d}""")
        ops = input("Elige una opción: ")
        SALIR = 0
        while SALIR == 0:
            try:
                ops = int(ops)  # a
                if ops in [1, 2, 3, 4]:
                    SALIR = 1
                else:
                    ops = input("Elige una opción correcta: ")
                    SALIR = 0
            except:
                ops = input("Elige una opción correcta: ")
                SALIR = 0
        # Match
        match ops:
            case 1:
                Gryffindor += 1
            case 2:
                Hufflepuff += 1
            case 3:
                Ravenclaw += 1
            case 4:
                Slytherin += 1

        all_questions.remove(random_question)

    maximo = {"Gryffindor": Gryffindor, "Hufflepuff": Hufflepuff,
              "Ravenclaw": Ravenclaw, "Slytherin": Slytherin}
    # print(maximo)
    maxi = list(maximo.values())

    for i, j in maximo.items():
        if np.max(maxi) == j:
            casa = i
            break

    print(f"""Apartir de ahora serás de la Casa {casa}!\n""")
    print("GRACIAS POR JUGAR!")


sorting_hat()
