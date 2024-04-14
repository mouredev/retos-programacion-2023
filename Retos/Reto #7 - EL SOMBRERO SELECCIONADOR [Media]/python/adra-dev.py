"""
Crea un programa que simule el comportamiento del sombrero
seleccionador del universo magico de Harry Potter.
- De ser posible realizara 5 preguntas (como minimo) a traves
de la terminal.
- Cada pregutna tendra 4 respuestas posibles (tambien a
selecciona una a traves de terminal).
- En guncion de las respuestas a las 5 preguntas deberas 
disenar un algoritmo que 
coloque al alumno en una de las 4 casas de Hogwarts
(Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
- Ten en cuenta los rasgos de cada casa para hacer las 
preguntas y crear el algoritmo seleccionador.
Por ejemplo, en Slytherin se premia la ambicion y la astucia.
"""

import random

# gryffindor: valor
# hufflepuff: lealtad
# ravenclaw: sabiduría
# slytherin: ambición


class HatQuestion:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers


def get_answer():

    answer = input("Responde 1, 2, 3 o 4: ")
    if answer == "1" or answer == "2" or answer == "3" or answer == "4":
        return int(answer)

    return get_answer()


print("Hola, soy el \"Sombrero Seleccionador\"\nTendrás que responder cinco preguntas para ayudarme a descubrir tu casa de Hogwarts.\n")

hat_questions = [HatQuestion("¿Cómo te definirías?", [
                            ("1. Valiente", "gryffindor"),
                            ("2. Leal", "hufflepuff"),
                            ("3. Sabio", "ravenclaw"),
                            ("4. Ambicioso", "slytherin")]),
                 HatQuestion("¿Cuál es tu clase favorita?", [
                            ("1. Vuelo", "gryffindor"),
                            ("2. Pociones", "ravenclaw"),
                            ("3. Defensa contra las artes oscuras", "slytherin"),
                            ("4. Animales fantásticos", "hufflepuff")]),
                 HatQuestion("¿Dónde pasarías más tiempo?", [
                            ("1. Invernadero", "hufflepuff"),
                            ("2. Biblioteca", "ravenclaw"),
                            ("3. En la sala común", "slytherin"),
                            ("4. Explorando", "gryffindor")]),
                 HatQuestion("¿Cuál es tu color favorito?", [
                            ("1. Rojo", "gryffindor"),
                            ("2. Azul", "ravenclaw"),
                            ("3. Verde", "slytherin"),
                            ("4. Amarillo", "hufflepuff")]),
                 HatQuestion("¿Cuál es tu mascota?", [
                            ("1. Sapo", "ravenclaw"),
                            ("2. Lechuza", "gryffindor"),
                            ("3. Gato", "hufflepuff"),
                            ("4. Serpiente", "slytherin")])]

houses = {
    "gryffindor": 0,
    "hufflepuff": 0,
    "ravenclaw": 0,
    "slytherin": 0
}

for hat_question in hat_questions:

    print(hat_question.question)
    for hat_answers in hat_question.answers:
        print(hat_answers[0])

    house = hat_question.answers[get_answer() - 1][1]
    houses[house] += 1

    print()

selected_house = []
max_points = 0

for house, points in houses.items():
    if points > max_points:
        selected_house.clear()
        selected_house.append(house)
        max_points = points
    elif points == max_points:
        selected_house.append(house)
        max_points = points

if len(selected_house) == 1:
    print(f"Lo tengo claro... ¡{selected_house[0].capitalize()}!")
else:
    print(
        f"Ha estado complicado... ¡{random.choice(selected_house).capitalize()}!")
