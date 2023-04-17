# * Crea un programa que simule el comportamiento del sombrero selccionador del
# * universo mágico de Harry Potter.
# * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
# *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
# *   Por ejemplo, en Slytherin se premia la ambición y la astucia.

import random

def get_response(question):
    possible_answers = ["a","b","c","d"]
    answer = ""
    while answer.lower() not in possible_answers:
        answer = input(question)
    return answer

def compare(score):
    if score.count(max(score)) != 1:
        tie(score)
    else:
        show_winner(score.index(max(score)))

def tie(score):
    tie_list = [i for i, num in enumerate(score) if num == max(score)]
    rand = random.choice(tie_list)
    show_winner(rand)      

def show_winner(index):
    if index == 0:
        print("\nCongratulations, you are from Gryffindor.")
    elif index == 1:
        print("\nCongratulations, you are from Slytherin.")
    elif index == 2:
        print("\nCongratulations, you are from Hufflepuff.")
    elif index == 3:
        print("\nCongratulations, you are from Ravenclaw.")

def count():
    score = [0,0,0,0]
    for answer in ANSWERS:
        if answer == "a":
            score[0] += 1
        elif answer == "b":
            score[1] += 1
        elif answer == "c":
            score[2] += 1
        elif answer == "d":
            score[3] += 1
    compare(score)

ANSWERS = []
questions = [
    "What is the most outstanding feature of our personality? \na) Bravery\nb) Ambition\nc)Loyalty\nd)Intelligence\n",
    "If you encounter an obstacle in your path, how would you face it? \na) Challenge it head-on\nb) Find a way to use it to my advantage\nc) Help others overcome it together\nd) Analyze and find a logical solution\n",
    "What kind of leader would you like to be? \na) One who inspires others to be brave\nb) One who controls and wields power\nc) One who is fair and concerned for everyone's well-being\nd) One who makes decisions based on wisdom and knowledge\n",
    "What would be your favorite subject at Hogwarts? \na) Defense Against the Dark Arts\nb) Potions\nc) Herbology\nd) Divination\n",
    "If you could have a magical animal as a pet, which would you choose? \na) A phoenix\nb) A basilisk\nc) A magical badger\nd) A magical eagle\n"
]
print("Welcome to the sorting hat program. You have to answer the next five questions with a,b,c or d.")
for question in questions:
    ANSWERS.append(get_response(question))
count()