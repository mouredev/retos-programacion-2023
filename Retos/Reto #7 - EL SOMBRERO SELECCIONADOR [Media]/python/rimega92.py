# Crea un programa que simule el comportamiento del sombrero selccionador del
# universo mágico de Harry Potter.
# - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#   coloque al alumno en una de las 4 casas de Hogwarts:
#   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# - Ten en cuenta los rasgos de cada casa para hacer las preguntas
#   y crear el algoritmo seleccionador:
#   Por ejemplo, en Slytherin se premia la ambición y la astucia.

def hacer_pregunta(pregunta, opciones):
    print(pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    respuesta = int(input("Selecciona tu respuesta (escribe el número): "))
    while respuesta not in range(1, len(opciones) + 1):
        respuesta = int(input("Respuesta inválida. Por favor, selecciona un número válido: "))
    return respuesta - 1

def sombrero_seleccionador():
    preguntas = [
        "¿Qué cualidad es más importante para ti?",
        "¿Qué tipo de animal te gustaría ser?",
        "¿Qué habilidad te gustaría tener?",
        "En una situación difícil, ¿qué harías?",
        "¿Qué lugar te llama más la atención?"
    ]

    opciones = [
        ["Valentía", "Ambición", "Lealtad", "Intelecto"],
        ["León", "Serpiente", "Tejón", "Águila"],
        ["Poder", "Astucia", "Paciencia", "Conocimiento"],
        ["Enfrentar el desafío directamente", "Planear cuidadosamente", "Apoyar a otros", "Analizar la situación"],
        ["Bosque oscuro", "Sala común de Slytherin", "Campo abierto", "Biblioteca"]
    ]

    puntajes = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    for i in range(5):
        respuesta = hacer_pregunta(preguntas[i], opciones[i])
        puntajes["Gryffindor"] += respuesta == 0  # Añade 1 punto si la respuesta es la opción 1
        puntajes["Slytherin"] += respuesta == 1  # Añade 1 punto si la respuesta es la opción 2
        puntajes["Hufflepuff"] += respuesta == 2  # Añade 1 punto si la respuesta es la opción 3
        puntajes["Ravenclaw"] += respuesta == 3  # Añade 1 punto si la respuesta es la opción 4

    casa_seleccionada = max(puntajes, key=puntajes.get)
    print(f"¡Eres de la casa {casa_seleccionada}!")

if __name__ == "__main__":
    sombrero_seleccionador()
