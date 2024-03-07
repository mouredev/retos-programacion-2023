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

def main():
    print("¡Bienvenido al Sombrero Seleccionador!")
    print("Responde las siguientes preguntas para saber a qué casa perteneces:")

    # Preguntas y respuestas
    preguntas = [
        "¿Prefieres la aventura o la estabilidad?",
        "¿Valoras la inteligencia o la lealtad?",
        # Agrega más preguntas aquí
    ]

    casas = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    for i, pregunta in enumerate(preguntas):
        print(f"\nPregunta {i + 1}: {pregunta}")
        print("1. Gryffindor")
        print("2. Slytherin")
        print("3. Hufflepuff")
        print("4. Ravenclaw")
        respuesta = int(input("Elige una opción (1-4): "))

        if respuesta in range(1, 5):
            casa = list(casas.keys())[respuesta - 1]
            casas[casa] += 1
        else:
            print("Opción inválida. Inténtalo de nuevo.")

    # Determina la casa
    casa_elegida = max(casas, key=casas.get)
    print(f"\n¡Eres parte de la casa {casa_elegida}!")

if __name__ == "__main__":
    main()
