import random

mansion = [
    ['🚪', '⬜', '⬜', '⬜'],
    ['⬜', '👻', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '👻'],
    ['⬜', '⬜', '🍭', '⬜']
]

def generar_enigma():
    enigmas = [
        {
            'pregunta': '¿Que es un vampiro?',
            'respuesta': 'un ser de la noche',
        },
        {
            'pregunta': '¿Cual es el color de una calabaza?',
            'respuesta': 'naranja',
        },
        {
            'pregunta': '¿Que animal se relaciona con Halloween?',
            'respuesta': 'murcielago',
        },
        {
        'pregunta': '¿Cuál es la tradición en Halloween en la que los niños van de casa en casa pidiendo dulces?',
        'respuesta': 'Truco o Trato',
        },
        {
            'pregunta': '¿En qué fecha se celebra Halloween?',
            'respuesta': '31 de octubre',
        },
        {
            'pregunta': '¿Qué fruta se usa comúnmente para tallar linternas en Halloween?',
            'respuesta': 'calabaza',
        },
        {
            'pregunta': '¿Cómo se llama la película animada de Halloween en la que Jack Skellington descubre la Navidad?',
            'respuesta': 'El Extraño Mundo de Jack',
        },
        {
            'pregunta': '¿Cuál es el disfraz más común en Halloween?',
            'respuesta': 'bruja',
        }
    ]
    return random.choice(enigmas)

def jugar():
    x, y = 0, 0  
    intentos = 1
    fantasmas = random.random() < 0.1  

    while True:
        habitacion = mansion[y][x]

        if habitacion == '🍭':
            print("¡Encontraste la habitación de los dulces! ¡Ganaste!")
            break

        print(f"Estás en una habitación {habitacion}.")
        if fantasmas:
            print("¡Un fantasma apareció! Debes responder dos preguntas para salir.")
            for _ in range(2):
                enigma = generar_enigma()
                respuesta_usuario = input(f"Pregunta {intentos}: {enigma['pregunta']} ").strip().lower()
                if respuesta_usuario == enigma['respuesta']:
                    print("Respuesta correcta. ¡El fantasma se ha ido!")
                else:
                    print("Respuesta incorrecta. El fantasma se burla de ti.")
                    break
                intentos += 1
            else:
                fantasmas = False   
        else:
            enigma = generar_enigma()
            respuesta_usuario = input(f"Pregunta {intentos}: {enigma['pregunta']} ").strip().lower()
            if respuesta_usuario == enigma['respuesta']:
                print("Respuesta correcta. Puedes moverte.")
                direccion = input("¿Hacia dónde quieres moverte (norte/sur/este/oeste)? ").strip().lower()
                if direccion == 'norte':
                    if y > 0:
                        y -= 1
                    else:
                        print("No puedes ir al norte desde aquí.")
                elif direccion == 'sur':
                    if y < 3:
                        y += 1
                    else:
                        print("No puedes ir al sur desde aquí.")
                elif direccion == 'este':
                    if x < 3:
                        x += 1
                    else:
                        print("No puedes ir al este desde aquí.")
                elif direccion == 'oeste':
                    if x > 0:
                        x -= 1
                    else:
                        print("No puedes ir al oeste desde aquí.")
                else:
                    print("Dirección no válida. Debes elegir norte, sur, este u oeste.")
            else:
                print("Respuesta incorrecta. No puedes avanzar.")
        intentos += 1

print("Bienvenido a la mansión abandonada. Tu misión es encontrar la habitación de los dulces.")
jugar()
