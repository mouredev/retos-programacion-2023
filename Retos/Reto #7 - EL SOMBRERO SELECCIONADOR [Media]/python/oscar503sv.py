import time

"""
Crea un programa que simule el comportamiento del sombrero seleccionador del
universo mágico de Harry Potter.
- De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
- Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
- En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
  coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
- Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
  Por ejemplo, en Slytherin se premia la ambición y la astucia.

    Gryffindor: valentía, disposición, coraje y caballerosidad
    Hufflepuff: leales, honestos y que no teman el trabajo pesado.
    Ravenclaw: creativos, curiosos y que siempre busquen la respuesta.
    Slytherin: ambición y la astucia.
"""

def ask_questions(houses: dict) -> dict:
    questions = {
        "¿Qué cualidad valoras más en un amigo?": "a. La valentía b. La astucia c. La sabiduría d. La lealtad",
        "\n¿Qué asignatura te resulta más interesante?": "a. Defensa contra las Artes Oscuras b. Pociones c. Astronomía d. Herbologia",
        "\n¿Qué tipo de tarea te resulta más satisfactoria?": "a. Superar tus propios limites b. Vencer a tus oponentes c. Descubrir nuevos conocimientos d. Ayudar a los demás",
        "\n¿Qué lugar te gustará explorar en Hogwarts?": "a. La Sala de los Menesteres b. Las Mazmorras c. La Biblioteca d. El Invernadero",
        "\n¿Qué te motiva a seguir adelante?": "a. La búsqueda de aventura b. La búsqueda de poder c. La búsqueda del conocimiento d. La búsqueda de la verdad",
    }

    for question in questions:
        while True:
            print(question)
            print(questions[question])
            answer = input("Respuesta: ").lower()
            if answer in ["a", "b", "c", "d"]:
                if answer == "a":
                    houses["Gryffindor"] += 1
                elif answer == "b":
                    houses["Hufflepuff"] += 1
                elif answer == "c":
                    houses["Ravenclaw"] += 1
                elif answer == "d":
                    houses["Slytherin"] += 1
                break
            else:
                print("\nRespuesta inválida")
    return houses


def hats_choice(houses: dict) -> str:
    max_points = max(houses.values())
    for house, points in houses.items():
        if points == max_points:
            return house

def main():
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    selected_house = hats_choice(ask_questions(houses))
    print("Ha sido una decisión muy difícil...")
    time.sleep(2)
    print("Pero...")
    time.sleep(2)
    print("Pero...")
    time.sleep(2)
    print(f"\nTu casa es: ¡{selected_house}!\n")

if __name__ == "__main__":
    main()
