'''
/*
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
 */
'''

import random

def generarMansion():
    mansion = [["⬜️" for _ in range(4)] for _ in range(4)]
    mansion[random.randint(0, 3)][random.randint(0, 3)] = "🚪"
    mansion[random.randint(0, 3)][random.randint(0, 3)] = "🍭"
    for _ in range(2):
        x, y = random.randint(0, 3), random.randint(0, 3)
        while mansion[x][y] != "⬜️":
            x, y = random.randint(0, 3), random.randint(0, 3)
        mansion[x][y] = "👻"
    return mansion

mansion = generarMansion()

def generarEnigma():
    enigmas = [
        {"pregunta": "¿Qué tiene ojos pero no puede ver?", "respuesta": "Una aguja"},
        {"pregunta": "¿Qué tiene alas pero no puede volar?", "respuesta": "Una carta"},
        {"pregunta": "¿Qué es algo que siempre sube y nunca baja?", "respuesta": "Tu edad"},
        {"pregunta": "¿Cuál es el animal más antiguo?", "respuesta": "La cebra"},
        {"pregunta": "Tengo ciudades, pero no tengo casas. Tengo montañas, pero no tengo árboles. Tengo agua, pero no barcos. ¿Qué soy?", "respuesta": "Un mapa"},
        {"pregunta": "Puedo ser largo o corto; puedo ser rápida o lenta. Puedo estar en tu mano o en tu pie. ¿Qué soy?", "respuesta": "Una sombra"},
        {"pregunta": "Todos me necesitan, pero a nadie le gusto. ¿Qué soy?", "respuesta": "Un consejo"},
        {"pregunta": "Siempre estoy delante de ti, pero no puedes verme. Nunca hablo, pero siempre te escucho. ¿Qué soy?", "respuesta": "Tu futuro"},
        {"pregunta": "¿Qué se puede romper, aunque nunca se haya dicho ni una palabra?", "respuesta": "Un corazón"},
        {"pregunta": "¿Qué tiene llaves pero no puede abrir cerraduras?", "respuesta": "Un piano"},
        {"pregunta": "Puedes encontrarme en la oscuridad, pero nunca en la luz. No tengo forma ni color, pero puedes sentarme en tu mano. ¿Qué soy?", "respuesta": "El sueño"},
        {"pregunta": "Tengo un mar pero no tengo agua. Tengo una jungla pero no tengo árboles. Tengo un desierto pero no tengo arena. ¿Qué soy?", "respuesta": "Un mapa del mundo"},
        {"pregunta": "Siempre estoy corriendo, pero nunca me canso. Siempre estoy hablando, pero nunca digo una palabra. ¿Qué soy?", "respuesta": "Un rio"},
        {"pregunta": "A veces soy fuerte y a veces soy débil. A veces tengo razón y a veces tengo que callar. ¿Qué soy?", "respuesta": "La voz"},
        {"pregunta": "Soy un agujero en el agua, pero mantengo el agua fuera. ¿Qué soy?", "respuesta": "Un barco"},
        {"pregunta": "Puedes romperme sin tocar ni una sola vez. ¿Qué soy?", "respuesta": "Un suspiro"}
    ]
    return random.choice(enigmas)

def resolverEnigma(enigma):
    print(enigma["pregunta"])
    respuestaUsuario = input("Tu respuesta: ").lower()
    if respuestaUsuario == enigma["respuesta"].lower():
        return True
    else:
        print("Respuesta incorrecta. Intenta de nuevo.")
        return False

def juego():
    print("¡Bienvenido a la mansión abandonada!\n Tu misión es encontrar la habitación de los dulces para salir.")
    x,y = 0,0
    while True:
        habitacion = mansion[x][y]
        if habitacion == "👻":
            print("¡Oh no! Te encuentras con un fantasma. Debes responder 2 preguntas para salir de la habitación")
            enigmaU = generarEnigma()
            enigmaD = generarEnigma()
            if resolverEnigma(enigmaU) and resolverEnigma(enigmaD):
                print("¡Respuestas correctas! Puedes continuar")
            else:
                print("¡Oh no! Has fallado, el fantasma te atrapa.")
                break
        elif habitacion == "⬜️":
            enigma = generarEnigma()
            while not resolverEnigma(enigma):
                enigma = generarEnigma()
            print("¡Enigma resuelto! Puedes continuar con tu búsqueda.")
        elif habitacion == "🍭":
            print("¡Felicidades! Has encontrado la habitación de los dulces. ¡Ganaste el juego!")
            break
        direccion = input("¿A dónde quieres ir? (norte/sur/oeste/este): ").lower()
        if direccion == "norte" and x > 0:
            x -= 1
        elif direccion == "sur" and x < 3:
            x += 1
        elif direccion == "este" and y < 3:
            y += 1
        elif direccion == "oeste" and y > 0:
            y -= 1
        else:
            print("Dirección no válida. Intenta de nuevo.")

juego()