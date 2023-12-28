'''/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 * Coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 * Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */'''


def sombrero():

    recuento = [0, 0, 0, 0]
    respuesta = ""
    print('Bienvenido al sombrero seleccionador de Hogwarts')
    print('Responde a las siguientes preguntas para saber a que casa perteneces')
    print('')
    print('Pregunta 1: ¿Que te gustaría ser?')
    print('1. Rico')   # Slitherin
    print('2. Sabio')  # Ravenclaw
    print('3. Fuerte')  # Griffindor
    print('4. Feliz')  # Hufflepuf

    while respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4':
        respuesta = input('Elige una opción: ')

        if respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4':
            print('Respuesta no válida')

        if respuesta == '1':
            recuento[0] += 1

        elif respuesta == '2':
            recuento[3] += 1

        elif respuesta == '3':
            recuento[1] += 1

        elif respuesta == '4':
            recuento[2] += 1

        else:
            print('Respuesta no válida')

    print('Pregunta 2: ¿Qué cualidad te parece más valiosa?:  ')
    print('1. Ambición')  # Slitherin
    print('2. Inteligencia')  # Ravenclaw
    print('3. Lealtad')  # Hufflepuff
    print('4. Valentía')  # Griffindor
    respuesta = ""

    while respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4':
        respuesta = input('Elige una opción: ')
        if respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4':
            print('Respuesta no válida')

        if respuesta == '1':
            recuento[0] += 1

        elif respuesta == '2':
            recuento[3] += 1

        elif respuesta == '3':
            recuento[2] += 1

        elif respuesta == '4':
            recuento[1] += 1

        else:
            print('Respuesta no válida')

    print('Pregunta 3: ¿Cuál de las siguientes opciones odiarías más que la gente te llamara?: ')
    print('1. Ignorante')  # Ravenclaw
    print('2. Cobarde')    # Griffindor
    print('3. Egoísta')   # Hufflepuff
    print('4. Ordinario')  # Slitherin
    respuesta = ""

    while respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4':
        respuesta = input('Elige una opción: ')
        if respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4':
            print('Respuesta no válida')

        if respuesta == '1':
            recuento[3] += 1

        elif respuesta == '2':
            recuento[1] += 1

        elif respuesta == '3':
            recuento[2] += 1

        elif respuesta == '4':
            recuento[0] += 1

        else:
            print('Respuesta no válida')

    print('Pregunta 4: ¿Después de su muerte ¿qué es lo que más te gustaría que hiciera la gente cuando escuche tu nombre?: ')
    print('1. Leer')  # Ravenclaw
    print('2. Hacer deporte')  # Griffindor
    print('3. Estar con tus amigos')  # Hufflepuff
    print('4. Estar solo')  # Slitherin

    respuesta = ""
    while respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4':
        respuesta = input('Elige una opción: ')
        if respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4':
            print('Respuesta no válida')

        if respuesta == '1':
            recuento[3] += 1

        elif respuesta == '2':
            recuento[1] += 1

        elif respuesta == '3':
            recuento[2] += 1

        elif respuesta == '4':
            recuento[0] += 1

        else:
            print('Respuesta no válida')


# Slitherin, Gryffindor, Hufflepuff, Ravenclaw
    print('Pregunta 5: Preferirías inventar una poción que garantizara: ')
    print('1. Amor')  # Hufflepuff
    print('2. Gloria')  # Gryffindor
    print('3. Sabiduría')  # Ravenclaw
    print('4. Poder')  # Slitherin
    respuesta = ""

    while respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4':
        respuesta = input('Elige una opción: ')
        if respuesta != '1' and respuesta != '2' and respuesta != '3' and respuesta != '4':
            print('Respuesta no válida')

        if respuesta == '1':  # Hufflepuff
            recuento[3] += 1

        elif respuesta == '2':  # Gryffindor
            recuento[1] += 1

        elif respuesta == '3':  # Ravenclaw
            recuento[2] += 1

        elif respuesta == '4':  # Slitherin
            recuento[0] += 1

        else:
            print('Respuesta no válida')

    if max(recuento) == recuento[0]:
        print('Tu casa es Slitherin')
    elif max(recuento) == recuento[1]:
        print('Tu casa es Gryffindor')
    elif max(recuento) == recuento[2]:
        print('Tu casa es Hufflepuff')
    elif max(recuento) == recuento[3]:
        print('Tu casa es Ravenclaw')
    else:
        print('Error')


sombrero()
