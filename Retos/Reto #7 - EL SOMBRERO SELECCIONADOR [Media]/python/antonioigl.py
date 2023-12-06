"""
/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
"""

houses = {1: 'Gryffindor', 2: 'Ravenclaw', 3: 'Slytherin', 4: 'Hufflepuff'}

questions: list[map] = [
    {
        'statement': 'Digamos que tiene un examen la próxima semana, ¿cómo te preparas?',
        'answers': {
            1: 'Reviso mis apuntes y estudio solo en mi casa',
            2: 'Dejo todo para última hora y el día antes me trasnocho estudiando con uno o dos amigos',
            3: 'Estudio un poquito cada día de la semana pero no me estreso porque sé que he parado bolas en clase '
               'entonces me va a ir bien',
            4: 'Le digo a mis compañeros que nos reunamos a estudiar juntos en la biblioteca'
        }
    },
    {
        'statement': 'Si su habitación en Hogwarts se está quemando y pudiera rescatar solo una cosa, ¿cuál sería?',
        'answers': {
            1: 'Su libro favorito o su computador',
            2: 'A su mascota',
            3: 'Una reliquia familiar que ha pasado de generación en generación',
            4: 'Las fotos que tiene con sus amigos',
        }
    },
    {
        'statement': '¿Cuál de estas cosas lo pone más nervioso?',
        'answers': {
            1: 'Los espacios cerrados',
            2: 'Hablar en público',
            3: 'La soledad',
            4: 'Fracasar',
        }
    },
    {
        'statement': 'Si le dan un pedazo de papel, ¿qué hace con él?',
        'answers': {
            1: 'Un avioncito de papel',
            2: 'Escribe',
            3: 'Dibuja',
            4: 'Lo rompe en muchos pedacitos',
        }
    },
    {
        'statement': '¿Qué cosa le fastidia más?',
        'answers': {
            1: 'Que la gente confunda ay, hay y ahí',
            2: 'Que la gente se indigne por cualquier tontería',
            3: 'Que la gente se aproveche de otra gente',
            4: 'Que la gente no sea leal',
        }
    }
]


def sorting_hat() -> str:
    houses_points: map(int, int) = {1: 0, 2: 0, 3: 0, 4: 0}

    for question in questions:
        print(f"Question: {question['statement']}")
        print('Options:')
        for key, answer in question['answers'].items():
            print(f"\t{key} - {answer}")

        while True:
            try:
                option = int(input('\nSelect 1, 2, 3 or 4: '))
                if option not in question['answers']:
                    print(f'Invalid option. Try again.')
                    continue
                break
            except ValueError:
                print(f'Invalid option. Try again.')

        houses_points[option] += 1

    return houses[max(houses_points, key=houses_points.get)]


if __name__ == "__main__":
    print(f"You're {sorting_hat()}")
