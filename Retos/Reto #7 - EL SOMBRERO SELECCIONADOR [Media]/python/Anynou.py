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

def question(q,r1,r2,r3,r4):
    print(" ")
    print(q)
    print(" ")
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(" ")
    answer = input("Introduce tu respuesta: ")

    return answer

def select_home(points):
    home = ""

    if points <= 4:
        home = "Gryffindor"
    elif points > 4 and points <= 8:
        home = "Slytherin"
    elif points > 8 and points <= 12:
        home = "Hufflepuff"
    else:
        home = "Ravenclaw"

    return home


questions = {
    1: ['¿Cuál de las siguientes opciones odiaría más que la gente lo llamara?', 'a - Ordinario', 'b - Ignorante ', 'c - Cobarde','d - Egoista'],
    2: ['Después de su muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?', 'a - Te extraña, pero sonríe', 'b - Pide mas historias sobre tus aventuras', 'c - Piensa con admiración tus logros', 'd - No me importa lo que la gente piense de mí después de mi muerte, es lo que piensan de mi mientras estoy vivo lo que cuenta'],
    3: ['Dada la opción, preferirías inventar una poción que garantizara:', 'a - Gloria', 'b - Sabiduría', 'c - Amor', 'd - Poder'],
    4: ['¿Cómo le gustaría ser conocido en la historia?', 'a - El sabio', 'b - El bueno', 'c - El gran', 'd - El audaz'],
    5: ['Entras en un jardín encantado. ¿Qué sería lo más curioso de examinar primero?', 'a - El árbol de hojas de plata con manzanas doradas', 'b - Las setas rojas gordas que parecen estar hablando entre sí', 'c - El estanque burbujeante en cuyas profundidades se arremolina algo luminoso', 'd - La estatua del viejo mago con un extraño centelleo en los ojos']
}

points = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

total_points = 0

for k,v in questions.items():
    answer = question(v[0], v[1], v[2], v[3], v[4])
    total_points += points[answer]

print("Tu casa es: %s" % select_home(total_points))
