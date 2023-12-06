puntuacion = {
    'Gryffindor': 0,
    'Slytherin': 0,
    'Hufflepuff': 0,
    'Ravenclaw': 0
}

preguntas = [
    { "enunciado": "¿Qué palabra te describe mejor?", "respuestas": { "Gryffindor": "Valentía", "Slytherin": "Lealtad", "Hufflepuff": "Liderazgo", "Ravenclaw": "Inteligencia" } },
    { "enunciado": "¿Qué opinas de los muggles?", "respuestas": { "Gryffindor": "Están bien en su mundo", "Slytherin": "Somos superiores a ellos", "Hufflepuff": "No deberían de existir", "Ravenclaw": "Me dan igual" } },
    { "enunciado": "¿Le temes al Señor Oscuro?", "respuestas": { "Gryffindor": "No, hay que defendernos de él", "Slytherin": "Sí, por eso hay que hacer lo que diga", "Hufflepuff": "Sí, me da mucho miedo", "Ravenclaw": "No, pero no me enfrentaría a él" } },
    { "enunciado": "¿A cuál de estos personajes admiras?", "respuestas": { "Gryffindor": "Minerva McGonagall", "Slytherin": "Severus Snape", "Hufflepuff": "Alastor Moody", "Ravenclaw": "Cedric Diggory" } },
    { "enunciado": "¿Sabes cuál es el primer nombre del fundador de la casa de Hufflepuff?", "respuestas": { "Gryffindor": "Hannah", "Slytherin": "Severus", "Hufflepuff": "Helga", "Ravenclaw": "Albus" } }
]

def seleccionar_pregunta(num: int = 1) -> dict:
    return preguntas[num]


def imprimir_pregunta(pregunta: dict):
    print(pregunta['enunciado'])
    i = 0
    for v in pregunta['respuestas'].values():
        i += 1
        print(f'\t{i}: {v}')


def sombrero_seleccionador():
    casa = sorted(puntuacion.items(), key=lambda item: item[1])[-1]
    return f'Tu casa es {casa[0]}'


def seleccionar_respuesta(pregunta: dict, respuesta: int):
    casa = list(pregunta['respuestas'].keys())[respuesta]
    puntuacion[casa] += 1


if __name__ == '__main__':
    for i in range(len(preguntas)):
        pregunta = seleccionar_pregunta(i)
        print(f'Pregunta #{i+1}', end=': ')
        imprimir_pregunta(pregunta)
        respuesta = int(input('Selecciona respuesta: '))
        seleccionar_respuesta(pregunta, respuesta-1)
        print()
    print(sombrero_seleccionador())
