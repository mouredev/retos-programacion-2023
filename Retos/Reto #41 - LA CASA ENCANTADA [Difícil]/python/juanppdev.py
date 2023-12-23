import random

# Función para generar un enigma aleatorio
def generar_enigma():
    enigmas = [
        {"pregunta": "¿Qué tiene llaves pero no puede abrir cerraduras?", "respuesta": "un piano"},
        {"pregunta": "¿Qué siempre sube y nunca baja?", "respuesta": "tu edad"},
        {"pregunta": "Tiene hojas, pero no es un árbol. ¿Qué es?", "respuesta": "un libro"},
        # Agrega más enigmas aquí
    ]
    return random.choice(enigmas)

# Función para resolver un enigma
def resolver_enigma(enigma):
    print(enigma["pregunta"])
    respuesta_usuario = input("Tu respuesta: ").lower()
    if respuesta_usuario == enigma["respuesta"]:
        print("¡Correcto! Puedes avanzar.")
        return True
    else:
        print("Respuesta incorrecta. No puedes avanzar.")
        return False

# Función para moverse
def moverse():
    direccion = input("¿A dónde quieres desplazarte? (norte/sur/este/oeste): ").lower()
    if direccion in ["norte", "sur", "este", "oeste"]:
        return direccion
    else:
        print("Dirección no válida. Inténtalo de nuevo.")
        return moverse()

# Función principal del juego
def juego():
    casa = [
        ["🚪", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "👻", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "👻"],
        ["⬜️", "⬜️", "🍭", "⬜️"]
    ]

    x, y = 0, 0  # Coordenadas iniciales
    dulces_x, dulces_y = 3, 2  # Coordenadas de la habitación de los dulces

    while True:
        habitacion_actual = casa[y][x]

        if x == dulces_x and y == dulces_y:
            print("¡Encontraste la habitación de los dulces! Has ganado.")
            break

        if habitacion_actual == "👻":
            print("¡Un fantasma te ha atrapado!")
            for _ in range(2):
                enigma = generar_enigma()
                if not resolver_enigma(enigma):
                    return
            print("El fantasma te deja ir. Elige una dirección para escapar.")
        elif habitacion_actual == "🍭":
            print("¡Estás en la habitación de los dulces!")
        else:
            enigma = generar_enigma()
            if not resolver_enigma(enigma):
                return

        direccion = moverse()

        if direccion == "norte" and y > 0:
            y -= 1
        elif direccion == "sur" and y < 3:
            y += 1
        elif direccion == "este" and x < 3:
            x += 1
        elif direccion == "oeste" and x > 0:
            x -= 1

if __name__ == "__main__":
    print("Bienvenido a la mansión abandonada. Tu misión es encontrar la habitación de los dulces.")
    juego()
