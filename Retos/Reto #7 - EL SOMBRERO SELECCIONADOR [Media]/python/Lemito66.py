"""
* Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia. 
"""


def sorting_hat():

    answers = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0
    }

    questions = {
        1: "¿Cuál es tu mayor fortaleza? \na. Coraje \nb. Ambición  \nc. Lealtad \nd. Inteligencia",
        2: "¿Qué habilidad te gustaría tener? \na. Ser un buen luchador \nb. Ser persuasivo/a y lograrlo   que quiero \nc. Tener un gran corazón y ayudar a los demás \nd. Ser muy astuto y resolver problemas complejos",
        3: "¿Cuál es tu mayor debilidad? \na. Ser muy valiente y arriesgado \nb. Ser muy ambicioso y egoísta \nc. Ser muy leal y no saber decir que no \nd. Ser muy inteligente y no saber decir que no",
        4: "¿Qué opinas de los desafíos? \na. Me encantan, siempre estoy buscando nuevos desafíos \nb. Son necesarios para llegar a la cima \nc. Pueden ser difíciles, pero los superaré con la ayuda de mis amigos \nd. Me gustan los desafíos que me permiten pensar y resolver problemas",
        5: "¿Qué valoras más en un amigo? \na. Coraje \nb. Ambición \nc. Lealtad \nd. Inteligencia",
    }

    for i in questions:
        print(
            f'Responde la pregunta {i} con la letra de la respuesta que más te identifique')
        print(questions[i])
        answer = input('Respuesta: ')

        if answer.lower() != 'a' and answer.lower() != 'b' and answer.lower() != 'c' and answer.lower() != 'd':
            print('Respuesta no válida')
            exit()
        else:
            answers[answer.lower()] += 1

    maximun_answer = max(answers, key=answers.get)

    return 'Gryffindor' if maximun_answer == 'a' else 'Slytherin' if maximun_answer == 'b' else 'Hufflepuff' if maximun_answer == 'c' else 'Ravenclaw'


print(sorting_hat())
