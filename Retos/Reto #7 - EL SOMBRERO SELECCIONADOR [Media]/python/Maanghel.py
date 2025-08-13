"""
Crea un programa que simule el comportamiento del sombrero selccionador del
    universo mágico de Harry Potter.
- De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
- Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
- En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
    coloque al alumno en una de las 4 casas de Hogwarts:
    (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
- Ten en cuenta los rasgos de cada casa para hacer las preguntas
    y crear el algoritmo seleccionador:
Por ejemplo, en Slytherin se premia la ambición y la astucia.
"""

from typing import List, Dict

def show_intro() -> None:
    """
    Displays the introduction message for the Hogwarts Sorting Hat quiz.
    """
    print(
        """
¡Bienvenido, joven mago o bruja!
Soy el Sombrero Seleccionador, encantado de conocerte.
Durante siglos he estado sobre las cabezas más brillantes, valientes, leales 
y astutas que han cruzado las puertas de Hogwarts.

Mi tarea no es fácil... pero siempre acierto.
Observo tu interior, leo tus pensamientos más profundos y descubro dónde realmente perteneces.
¿Serás un valiente Gryffindor, un sabio Ravenclaw, un leal Hufflepuff o un ambicioso Slytherin?

Responde con sinceridad...
Y deja que el Sombrero decida.
        """
    )

def ask_questions(questions: Dict[str, list[str | list[str]]]) -> dict[int, int]:
    """
    Asks the quiz questions to the user and records their answers.

    Args:
        questions (dict): A dictionary where keys are question IDs and values are
                        lists containing the question text and possible answers.

    Returns:
        dict: A dictionary with the count of answers for each house option.
    """
    scores = {1: 0, 2: 0, 3: 0, 4: 0}
    input("Presionar una tecla para continuar...")

    for number, (question_text, options) in questions.items():
        print(f"\nPregunta {number}: {question_text}")
        for i, answer in enumerate(options, 1):
            print(f"{i}. {answer}")

        while True:
            try:
                selection = int(input(">>> "))
                if selection in scores:
                    scores[selection] += 1
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("Error: Ingrese un valor de respuesta correcto.")

    return scores

def determine_house(scores: Dict[int, int], houses: List[str]) -> str:
    """
    Determines the Hogwarts house based on the highest score.

    Args:
        scores (dict): Dictionary with counts for each house option.
        houses (list): List of house names.

    Returns:
        str: The message revealing the assigned house.
    """
    max_selection = max(scores, key=lambda k: scores[k])

    match max_selection:
        case 1:
            return f"\n¡Ah, valiente de corazón y espíritu indomable… no hay duda… ¡{houses[0].upper()}!"
        case 2:
            return f"\nMente aguda, curiosa y brillante… solo un destino es digno de ti: ¡{houses[1].upper()}!"
        case 3:
            return f"\nUn alma justa, trabajadora y leal… sé exactamente dónde vas: ¡{houses[2].upper()}!"
        case 4:
            return f"\nAmbición, astucia y una voluntad de hierro… lo tengo claro: ¡{houses[3].upper()}!"
        case _:
            return "Hubo un error en el proceso de selección, por favor intenta nuevamente."

def sorting_hat() -> str:
    """
    Runs the Hogwarts Sorting Hat quiz and returns the house result.

    Returns:
        str: The final result message indicating the assigned Hogwarts house.
    """
    houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
    questions = {
        "1": ["¿Cuál de estas cualidades valoras más en una persona?",
            ["Valentía y coraje", "Inteligencia y sabiduría", "Lealtad y honestidad", "Ambición y determinación"]],
        "2": ["¿Qué tipo de rol prefieres en un grupo de trabajo?",
            ["El líder que toma riesgos y guía al equipo", "El que aporta ideas brillantes y soluciones creativas",
            "El que trabaja duro y mantiene al equipo unido", "El que organiza todo para asegurarse de que el grupo gane"]],
        "3": ["Si te encontraras con un problema difícil, ¿cómo lo enfrentarías?",
            ["Con valentía, enfrentándolo de frente", "Analizando todas las posibilidades primero",
            "Pidiendo ayuda y colaborando con otros", "Buscando una estrategia para salir beneficiado"]],
        "4": ["¿Qué animal mágico te gustaría tener como compañero?",
            ["Un fénix leal y valiente", "Un cuervo sabio que te dé consejos",
            "Un tejón que te acompañe siempre", "Una serpiente astuta y poderosa"]],
        "5": ["¿Cuál de estos lemas podría ser tuyo?",
            ['"Actúa, incluso si tienes miedo"', '"El conocimiento es poder"',
            '"Siempre estaré para quienes me necesiten"', '"El fin justifica los medios"']]
    }

    show_intro()
    scores = ask_questions(questions)
    return determine_house(scores, houses)


if __name__ == "__main__":
    print(sorting_hat())
