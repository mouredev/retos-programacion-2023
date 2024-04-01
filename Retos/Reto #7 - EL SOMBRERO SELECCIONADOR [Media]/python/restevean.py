"""
Ejercicio
"""


def sorting_hat():
    print(
        "Bienvenido al cuestionario del Sombrero Seleccionador. Responde las siguientes preguntas para descubrir a "
        "qué casa de Hogwarts perteneces.\n")

    # Questions and options.
    questions = [
        {
            "question": "Cuando te enfrentas a un desafío, tu primer pensamiento es:",
            "options": {
                "a": ("Enfrentarlo con valentía, sin importar las dificultades", "Gryffindor"),
                "b": ("Buscar la solución más eficiente, incluso si eso significa tomar atajos", "Slytherin"),
                "c": ("Mantener la calma y usar tu conocimiento para encontrar una solución", "Ravenclaw"),
                "d": ("Pedir ayuda a tus amigos, creyendo en el poder del trabajo en equipo", "Hufflepuff")
            }
        },
        {
            "question": "Lo que más valoras en ti mismo es:",
            "options": {
                "a": ("Tu lealtad a tus amigos y seres queridos", "Hufflepuff"),
                "b": ("Tu habilidad para alcanzar tus metas, no importa los obstáculos", "Slytherin"),
                "c": ("Tu valentía y capacidad para defender lo que crees correcto", "Gryffindor"),
                "d": ("Tu curiosidad y amor por el aprendizaje", "Ravenclaw")
            }
        },
        {
            "question": "En un proyecto en equipo, tú eres el que:",
            "options": {
                "a": ("Toma la iniciativa y lidera al grupo hacia el objetivo", "Gryffindor"),
                "b": ("Se asegura de que todos estén trabajando juntos armoniosamente", "Hufflepuff"),
                "c": ("Piensa en estrategias y planes detallados", "Ravenclaw"),
                "d": (
                    "Busca obtener los mayores beneficios, incluso si eso significa ser un poco competitivo",
                    "Slytherin")
            }
        },
        {
            "question": "Si pudieras elegir, preferirías:",
            "options": {
                "a": ("Ser recordado por tus heroicas aventuras", "Gryffindor"),
                "b": ("Ser recordado por tu poder y éxito", "Slytherin"),
                "c": ("Ser recordado por tu bondad y tu corazón", "Hufflepuff"),
                "d": ("Ser recordado por tus descubrimientos e inventos", "Ravenclaw")
            }
        },
        {
            "question": "Elige un objeto mágico:",
            "options": {
                "a": ("La espada de Gryffindor", "Gryffindor"),
                "b": ("El diario de Tom Riddle", "Slytherin"),
                "c": ("Un giratiempo", "Ravenclaw"),
                "d": ("La capa de invisibilidad", "Hufflepuff")
            }
        }
    ]

    # House scores
    houses = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    # Loop through each question
    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(f"{option}: {question['options'][option][0]}")
        response = input("Tu respuesta (a, b, c, d): ").lower()

        # Update the score for the selected house
        selected_house = question["options"][response][1]
        houses[selected_house] += 1

    # Determine the house with the highest score
    final_house = max(houses, key=houses.get)
    print(f"\n¡Felicidades! El Sombrero Seleccionador te ha asignado a: {final_house}")


if __name__ == "__main__":
    sorting_hat()
