# Reto #7: El sombrero seleccionador

#
# Crea un programa que simule el comportamiento del sombrero seleccionador del universo mágico de Harry Potter.
# - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
# Por ejemplo, en Slytherin se premia la ambición y la astucia.
#  

def hacer_pregunta(pregunta, opciones):
    print(pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    
    respuesta = input("Selecciona tu respuesta (1-4): ")
    while not respuesta.isdigit() or int(respuesta) not in range(1, 5):
        print("Respuesta no válida. Introduce un número del 1 al 4.")
        respuesta = input("Selecciona tu respuesta (1-4): ")
    
    return int(respuesta)

def sombrero_seleccionador():
    preguntas = [
        ("¿Qué cualidad valoras más?", ["Valentía", "Astucia", "Lealtad", "Intelecto"]),
        ("¿Qué animal prefieres?", ["León", "Serpiente", "Tejón", "Águila"]),
        ("¿Cómo te describirían tus amigos?", ["Audaz", "Ambicioso", "Leal", "Inteligente"]),
        ("¿Qué lugar prefieres?", ["Bosque", "Mazmorra", "Campo", "Torre"]),
        ("¿Qué harías si encuentras una llave de oro?", ["Intentar abrirla", "Ignorarla", "Protegerla", "Estudiarla"])
    ]

    respuestas = []

    for pregunta, opciones in preguntas:
        respuesta = hacer_pregunta(pregunta, opciones)
        respuestas.append(respuesta)

    # Lógica del sombrero seleccionador
    puntajes = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    for i, casa in enumerate(puntajes):
        puntajes[casa] += respuestas[i]

    casa_seleccionada = max(puntajes, key=puntajes.get)
    print(f"\n¡Bienvenido a {casa_seleccionada}!")

if __name__ == "__main__":
    sombrero_seleccionador()
