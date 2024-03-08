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

def hacer_pregunta(pregunta, opciones):
    print(pregunta)
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
    
    while True:
        try:
            respuesta = int(input("Selecciona tu respuesta (1-4): "))
            if 1 <= respuesta <= 4:
                return respuesta
            else:
                print("Por favor, ingresa un número válido.")
        except ValueError:
            print("Por favor, ingresa un número entero.")

def sombrero_seleccionador():
    preguntas = [
        "¿Qué cualidad valoras más en un amigo?",
        "¿Qué tipo de magia prefieres?",
        "En una situación difícil, ¿qué harías?",
        "¿Qué animal mágico te gustaría tener como mascota?",
        "¿Cuál es tu asignatura favorita en Hogwarts?"
    ]

    respuestas_casas = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    for pregunta in preguntas:
        respuesta = hacer_pregunta(pregunta, ["Valentía", "Ambición", "Lealtad", "Inteligencia"])

        if pregunta == preguntas[0]:
            respuestas_casas["Gryffindor"] += respuesta
            respuestas_casas["Slytherin"] += respuesta
        elif pregunta == preguntas[1]:
            respuestas_casas["Slytherin"] += respuesta
            respuestas_casas["Ravenclaw"] += respuesta
        elif pregunta == preguntas[2]:
            respuestas_casas["Gryffindor"] += respuesta
            respuestas_casas["Hufflepuff"] += respuesta
        elif pregunta == preguntas[3]:
            respuestas_casas["Slytherin"] += respuesta
            respuestas_casas["Hufflepuff"] += respuesta
        elif pregunta == preguntas[4]:
            respuestas_casas["Ravenclaw"] += respuesta
            respuestas_casas["Hufflepuff"] += respuesta

    casa_seleccionada = max(respuestas_casas, key=respuestas_casas.get)
    print(f"\n¡Bienvenido a {casa_seleccionada}!")

if __name__ == "__main__":
    print("Bienvenido al Simulador del Sombrero Seleccionador")
    sombrero_seleccionador()
