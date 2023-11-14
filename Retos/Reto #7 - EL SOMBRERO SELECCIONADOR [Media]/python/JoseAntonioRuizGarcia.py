quiz_harry_potter = {
    'Pregunta 1': {
        'texto': '¿Qué cualidad valoras más?',
        'opciones': {
            1: {
                'texto': 'Opción 1: Coraje',
                'respuesta': 'Gryffindor'
            },
            2: {
                'texto': 'Opción 2: Ambición',
                'respuesta': 'Slytherin'
            },
            3: {
                'texto': 'Opción 3: Lealtad',
                'respuesta': 'Hufflepuff'
            },
            4: {
                'texto': 'Opción 4: Intelecto',
                'respuesta': 'Ravenclaw'
            }
        }
    },
    'Pregunta 2': {
        'texto': 'Elige una mascota mágica:',
        'opciones': {
            1: {
                'texto': 'Opción 1: León',
                'respuesta': 'Gryffindor'
            },
            2: {
                'texto': 'Opción 2: Serpiente',
                'respuesta': 'Slytherin'
            },
            3: {
                'texto': 'Opción 3: Tejón',
                'respuesta': 'Hufflepuff'
            },
            4: {
                'texto': 'Opción 4: Águila',
                'respuesta': 'Ravenclaw'
            }
        }
    },
    'Pregunta 3': {
        'texto': '¿Qué tipo de libros prefieres?',
        'opciones': {
            1: {
                'texto': 'Opción 1: Aventuras emocionantes',
                'respuesta': 'Gryffindor'
            },
            2: {
                'texto': 'Opción 2: Misterio y astucia',
                'respuesta': 'Slytherin'
            },
            3: {
                'texto': 'Opción 3: Historias reconfortantes',
                'respuesta': 'Hufflepuff'
            },
            4: {
                'texto': 'Opción 4: Conocimiento profundo',
                'respuesta': 'Ravenclaw'
            }
        }
    },
    'Pregunta 4': {
        'texto': 'Elige una asignatura favorita:',
        'opciones': {
            1: {
                'texto': 'Opción 1: Defensa Contra las Artes Oscuras',
                'respuesta': 'Gryffindor'
            },
            2: {
                'texto': 'Opción 2: Pociones',
                'respuesta': 'Slytherin'
            },
            3: {
                'texto': 'Opción 3: Cuidado de Criaturas Mágicas',
                'respuesta': 'Hufflepuff'
            },
            4: {
                'texto': 'Opción 4: Adivinación',
                'respuesta': 'Ravenclaw'
            }
        }
    },
    'Pregunta 5': {
        'texto': '¿Cuál es tu color favorito?',
        'opciones': {
            1: {
                'texto': 'Opción 1: Rojo',
                'respuesta': 'Gryffindor'
            },
            2: {
                'texto': 'Opción 2: Verde',
                'respuesta': 'Slytherin'
            },
            3: {
                'texto': 'Opción 3: Amarillo',
                'respuesta': 'Hufflepuff'
            },
            4: {
                'texto': 'Opción 4: Azul',
                'respuesta': 'Ravenclaw'
            }
        }
    }
}

def quizHarryPotter() -> None:
    houses = ['Gryffindor', 'Slytherin' , 'Hufflepuff', 'Ravenclaw']
    houses_count = []
    answers = []

    for question in quiz_harry_potter:
        print(question)
        print(quiz_harry_potter[question].get('texto'))

        for option in quiz_harry_potter[question].get('opciones'):
            print(quiz_harry_potter[question]['opciones'][option].get('texto'))
        
        validation = range(1, 5)
        option_selected = 0

        while option_selected not in validation:
            option_selected = input('Introduce una respuesta: ')

            if option_selected.isnumeric():
                option_selected = int(option_selected)
        
        answers.append(quiz_harry_potter[question]['opciones'][option_selected].get('respuesta'))
        print('')
    
    for house in houses:
        count = answers.count(house)
        houses_count.append([house, count])
        houses_sort = sorted(houses_count, key=lambda x: x[1], reverse=True)
        house_selected = houses_sort[0][0]

    print(f'El sombrero te ha asignado la casa {house_selected}')

if __name__ == '__main__':
    quizHarryPotter()
