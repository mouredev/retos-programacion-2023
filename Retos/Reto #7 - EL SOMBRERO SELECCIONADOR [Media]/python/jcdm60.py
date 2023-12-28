
# Crea un programa que simule el comportamiento del sombrero selccionador del
# universo mágico de Harry Potter.
# - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#   Por ejemplo, en Slytherin se premia la ambición y la astucia.

def pregunta():
    respuestas = []
    valor_respuestas = {"a": 10, "b": 8, "c": 6, "d": 4}
    total = 0

    preguntas = [
        {
            "pregunta": "¿Cuál de las siguientes opciones odiaría más que la gente lo llamara?",
            "opciones": {'a': 'Ordinario', 'b': 'Ignorante', 'c': 'Cobarde', 'd': 'Egoísta'}
        },
        {
            "pregunta": "¿Dada la opción, preferirías inventar una poción que garantizara?",
            "opciones": {'a': 'Gloria', 'b': 'Sabiduria', 'c': 'Amor', 'd': 'Poder'}
        },
        {
            "pregunta": "¿Cómo le gustaría ser conocido en la historia?",
            "opciones": {'a': 'El sabio', 'b': 'El bueno', 'c': 'El gran', 'd': 'El audaz'}
        },
        {
            "pregunta": "¿Qué tipo de instrumento agrada más a tu oído?",
            "opciones": {'a': 'Violin', 'b': 'Tambores', 'c': 'Piano', 'd': 'Trompeta'}
        },
        {
            "pregunta": "¿Cuál preferirías ser?",
            "opciones": {'a': 'De confianza', 'b': 'Querido', 'c': 'Imitado', 'd': 'Alabado'}
        },
    ]

    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for key, value in pregunta["opciones"].items():
            print(f"{key}.- {value}")
        respuesta = input("Seleccione una opción (a, b, c o d): ").lower()
        while respuesta not in pregunta["opciones"]:
            print("Respuesta inválida. Por favor seleccione una de las opciones (a, b, c o d)")
            respuesta = input("Seleccione una opción (a, b, c o d): ").lower()
        respuestas.append(respuesta)

    for i in respuestas:
        if i in valor_respuestas:
            total += valor_respuestas[i]

    print(f"Puntaje total: {total}")

    if total >= 45:
        print("Perteneces a la casa Gryffindor!")
    elif total >= 38:
        print("Perteneces a la casa Hufflepuff!")
    elif total >= 31:
        print("Perteneces a la casa Slytherin!")
    else:
        print("Perteneces a la casa Ravenclaw!")

if __name__ == "__main__":
    pregunta()
