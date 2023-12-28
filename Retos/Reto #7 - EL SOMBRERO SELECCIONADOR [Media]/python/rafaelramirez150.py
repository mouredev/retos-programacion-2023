'''
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
 '''

def realizar_pregunta(pregunta, respuestas):
    print(pregunta)
    for i, respuesta in enumerate(respuestas):
        print(f"{i + 1}. {respuesta}")
    seleccion = int(input("Selecciona tu respuesta (1-4): "))
    return seleccion

def seleccionar_casa(respuestas):
    puntajes = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    # Realizar preguntas y sumar puntajes
    preguntas = [
        "¿Qué cualidad valoras más en ti mismo?",
        "¿Cuál es tu materia favorita en la escuela?",
        "¿Qué tipo de animal te gusta más?",
        "¿En qué tipo de ambiente te sientes más cómodo?",
        "¿Qué te gustaría hacer en tu tiempo libre?"
    ]
    opciones = [
        ["Valentía", "Astucia", "Lealtad", "Inteligencia"],
        ["Defensa Contra las Artes Oscuras", "Pociones", "Cuidado de Criaturas Mágicas", "Adivinación"],
        ["León", "Serpiente", "Tejón", "Águila"],
        ["Lugares con acción y aventura", "Lugares oscuros y misteriosos", "Lugares acogedores y tranquilos", "Lugares intelectuales y creativos"],
        ["Practicar deportes mágicos", "Investigar secretos oscuros", "Ayudar a otros", "Leer y estudiar"]
    ]

    for i in range(5):
        respuesta = realizar_pregunta(preguntas[i], opciones[i])
        puntajes["Gryffindor"] += respuesta == 1
        puntajes["Slytherin"] += respuesta == 2
        puntajes["Hufflepuff"] += respuesta == 3
        puntajes["Ravenclaw"] += respuesta == 4

    # Determinar la casa ganadora
    casa_ganadora = max(puntajes, key=puntajes.get)
    return casa_ganadora

# Ejecutar el programa
print("¡Bienvenido al Sombrero Seleccionador de Hogwarts!")
print("Responde las siguientes preguntas para determinar tu casa en Hogwarts.")

casa_seleccionada = seleccionar_casa(["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"])

print("¡El Sombrero ha decidido!")
print("Tu casa en Hogwarts es:", casa_seleccionada)