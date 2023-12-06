"""
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
"""

casas = [['Ravenclaw', 0], ['Gryffindor', 0],
         ['Hufflepuff', 0], ['Slytherin', 0]]
max = 0
answer = ''


preguntas = {
    '¿Cuál es tu asignatura favorita?': {
        'Astronomía': '-1)',
        'Defensa Contra las Artes Oscuras': '-2)',
        'Herbología': '-3)',
        'Pociones': '-4)'
    },
    '¿Qué lugar de Hogwarts te gustaría explorar más?': {
        'La Biblioteca': '-1)',
        'La Sala Común de Gryffindor': '-2)',
        'El Invernadero de Herbología': '-3)',
        'Las Mazmorras': '-4)'
    },
    '¿Qué animal te gusta más?': {
        'Águila': '-1)',
        'León': '-2)',
        'Tejón': '-3)',
        'Serpiente': '-4)'
    },
    '¿Cuál de estas frases te describe mejor?': {
        'La curiosidad me lleva por nuevos caminos': '-1)',
        'La valentía siempre es lo primero': '-2)',
        'Trabajando juntos se logran grandes cosas': '-3)',
        'El fin justifica los medios': '-4)'
    },
    '¿Qué cualidad te describe mejor?': {
        'Inteligencia': '-1)',
        'Valentía': '-2)',
        'Lealtad': '-3)',
        'Astucia': '-4)'
    }
}

print("¡Bienvenido al Sombrero Seleccionador de Hogwarts!")
for pregunta, respuestas in preguntas.items():
    print(pregunta)
    for res, option in respuestas.items():
        print(f"{option} {res}")
    alt = input('Seleccione una opcion: ')
    while (not (0 <= int(alt) and int(alt) <= 4 and len(alt) == 1)):
        alt = input('Seleccione una opcion: ')

    if (alt == '1'):
        casas[0][1] = casas[0][1] + 1
    elif (alt == '2'):
        casas[1][1] = casas[1][1] + 1
    elif (alt == '3'):
        casas[2][1] = casas[2][1] + 1
    elif (alt == '4'):
        casas[3][1] = casas[3][1] + 1

for i in casas:
    if (i[1] > max):
        max = i[1]
        answer = i[0]
print('************************************')
print(f'Perteneces a la casa {answer}')
print('************************************')

print("¡Gracias por utilizar el Sombrero Seleccionador de Hogwarts!")
