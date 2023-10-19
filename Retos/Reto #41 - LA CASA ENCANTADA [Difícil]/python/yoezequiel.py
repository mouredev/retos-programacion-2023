import random

# Enigmas y respuestas
enigmas = {
    "¿Qué criatura chupa la sangre en Halloween?": "Vampiro",
    "¿Cuál es el disfraz más común en Halloween para los niños?": "Calabaza",
    "¿Qué animal negro a menudo se asocia con la brujería en Halloween?": "Gato",
    "¿Qué se usa para iluminar las calabazas talladas en Halloween?": "Vela",
    "¿Qué dulce se recoge en bolsas en Halloween?": "Caramelo",
    "¿Qué sonrisa siniestra se talla en una calabaza de Halloween?": "Grimace",
    "¿Qué criatura de la noche se convierte en murciélago en Halloween?": "Drácula",
    "¿Qué elemento se usa para crear una atmósfera espeluznante en Halloween?": "Niebla",
    "¿Qué actividad consiste en buscar dulces de casa en casa en Halloween?": "Truco",
    "¿Qué espíritu errante regresa en Halloween según la leyenda?": "Fantasma"
}


# Mapa de la casa
habitaciones = [
    ["🚪", "⬜", "⬜", "⬜"],
    ["⬜", "👻", "⬜", "⬜"],
    ["⬜", "⬜", "⬜", "👻"],
    ["⬜", "⬜", "🍭", "⬜"],
]

# Posición inicial
posicion_x = 0
posicion_y = 0

# Función para mostrar el mapa y las opciones de movimiento
def mostrar_mapa_y_opciones():
    for i, fila in enumerate(habitaciones):
        if i == posicion_x:
            fila = [f"👣" if j ==
                    posicion_y else habitacion for j, habitacion in enumerate(fila)]
        print(" ".join(fila))
    print()

# Función para responder preguntas
def responder_pregunta(pregunta, respuesta_correcta):
    intentos = 3
    while intentos > 0:
        respuesta = input(f"{pregunta}: ").strip().lower()
        if respuesta == respuesta_correcta.lower():
            print("¡Correcto!")
            return True
        else:
            intentos -= 1
            print(f"Respuesta incorrecta. Te quedan {intentos} intentos.")
    print("Has agotado tus intentos. Debes responder esta pregunta para salir.")
    return False

# Función para manejar la aparición de un fantasma
def manejar_fantasma():
    mostrar_mapa_y_opciones()
    print("¡Un fantasma ha aparecido en la habitación!")

    # Preguntas del fantasma
    pregunta1 = random.choice(list(enigmas.keys()))
    respuesta1 = enigmas[pregunta1]
    pregunta2 = random.choice(list(enigmas.keys()))
    respuesta2 = enigmas[pregunta2]

    print(f"Pregunta 1: {pregunta1}")
    if not responder_pregunta(pregunta1, respuesta1):
        return False

    print(f"Pregunta 2: {pregunta2}")
    if not responder_pregunta(pregunta2, respuesta2):
        return False

    print("¡Escapaste del fantasma! Puedes continuar tu búsqueda.")
    return True


# Juego
while True:
    mostrar_mapa_y_opciones()
    enigma = random.choice(list(enigmas.keys()))
    print(f"Enigma: {enigma}")

    respuesta = input("Tu respuesta: ").strip().lower()

    if respuesta == enigmas[enigma].lower():
        print("¡Correcto! Puedes moverte en una dirección.")
        opciones = []
        if posicion_x > 0:
            opciones.append("norte")
        if posicion_x < 3:
            opciones.append("sur")
        if posicion_y > 0:
            opciones.append("oeste")
        if posicion_y < 3:
            opciones.append("este")
        print("Opciones de movimiento:", ", ".join(opciones))

        direccion = input("¿Hacia dónde quieres moverte? ").strip().lower()

        if direccion == "norte" and "norte" in opciones:
            posicion_x -= 1
        elif direccion == "sur" and "sur" in opciones:
            posicion_x += 1
        elif direccion == "este" and "este" in opciones:
            posicion_y += 1
        elif direccion == "oeste" and "oeste" in opciones:
            posicion_y -= 1
        else:
            print("Movimiento no válido. Intenta de nuevo.")
    else:
        print("Respuesta incorrecta. Intenta de nuevo.")

    if habitaciones[posicion_x][posicion_y] == "👻":
        if not manejar_fantasma():
            print(
                "El fantasma no te ha dejado avanzar. Debes responder las preguntas correctamente.")

    if habitaciones[posicion_x][posicion_y] == "🍭":
        mostrar_mapa_y_opciones()
        print(
            "¡Felicidades! Has encontrado la habitación de los dulces. ¡Ganaste el juego!")
        break
