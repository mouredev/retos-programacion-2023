"""
/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
"""
import sys


def ask_questions():
    dict_answers = {"gryffindor": 0, "slytherin": 0, "ravenclaw": 0, "hufflepuff": 0}
    dict_answers = question_1(dict_answers)
    dict_answers = question_2(dict_answers)
    dict_answers = question_3(dict_answers)
    dict_answers = question_4(dict_answers)
    dict_answers = question_5(dict_answers)
    return dict_answers


def check_answer(answer, dict_answers):
    match answer:
        case "a":
            dict_answers["gryffindor"] += 1

        case "b":
            dict_answers["ravenclaw"] += 1

        case "c":
            dict_answers["slytherin"] += 1

        case "d":
            dict_answers["hufflepuff"] += 1
        case _:
            sys.exit("Respuesta Incorrecta: El sombrero te ha rechazado")
    return dict_answers


def question_1(dict_answers):
    answer = input(
        "\nCual es tu principal caracteristica como mago? \n a) Valiente \n b) Intelectual \n c) Astuto \n d) Trabajador \n Respuesta: "
    )
    return check_answer(answer, dict_answers)


def question_2(dict_answers):
    answer = input(
        "\nSi alguien te ataca con un hechizo que haces? \n a) Le confrontas \n b) Lo esquivas \n c) Contraatacas desde un punto que no te vea \n d) Lo paras y aguantas hasta que se canse \n Respuesta: "
    )
    return check_answer(answer, dict_answers)


def question_3(dict_answers):
    answer = input(
        "\nCual es tu principal aspiración en la vida? \n a) Ser feliz y no tener miedo de nada \n b) Tener mucho conocimiento y ayudar a los demás \n c) Ser rico y poderoso \n d) Enseñar a los demas tus conocimientos \n Respuesta: "
    )
    return check_answer(answer, dict_answers)


def question_4(dict_answers):
    answer = input(
        "\nQuien es tu mago preferido del pasado? \n a) Minerva McGonagall \n b) Filius Flitwick \n c) Horace Slughorn \n d) Pomona Sprout \n Respuesta: "
    )
    return check_answer(answer, dict_answers)


def question_5(dict_answers):
    answer = input(
        "\nCual es tu animal preferido \n a) León \n b) Me gustan los pajaros \n c) Serpiente \n d) Uno adorable \n Respuesta: "
    )
    return check_answer(answer, dict_answers)


def main():
    dict = ask_questions()
    house = max(dict, key=dict.get).capitalize()
    print(f"\nEl sombrero ha elegido {house} como tu casa\n")


if __name__ == "__main__":
    main()
