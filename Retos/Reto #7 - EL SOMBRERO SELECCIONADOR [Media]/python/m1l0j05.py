# Crea un programa que simule el comportamiento del sombrero selccionador del
# universo mágico de Harry Potter.
# - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#   Por ejemplo, en Slytherin se premia la ambición y la astucia.


import time

### Quizz and answer ###
QUIZZ = {
    'query_1' : '¿Qué cualidad valoras más en ti mismo/a?',
    'query_2':'¿Qué tipo de actividad disfrutas más?',
    'query_3':'¿Cuál es tu materia favorita en la escuela?',
    'query_4':'¿Qué animal te parece más interesante?',
    'query_5':'¿Cómo describirías tu personalidad en una palabra?',
    'query_6':'¿Cuál es tu mayor objetivo en la vida?',
    'query_7':'¿Qué cualidad te describe mejor?',
    'query_8':'¿Cuál de estas criaturas mágicas te gustaría tener como mascota?',
    'query_9':'¿Qué asignatura de Hogwarts te resulta más interesante?',
    'query_10':'¿Qué valoras más en una persona?',
}

ANSWER = {
    'answer_1':{
        'Valentía':'Gryffindor',
        'Astucia':'Slytherin',
        'Lealtad':'Hufflepuff',
        'Inteligencia':'Ravenclaw',
    },
    'answer_2':{
        'Deportes y juegos de riesgo':'Gryffindor',
        'Resolver acertijos y enigmas':'Ravenclaw',
        'Ayudar a otros y trabajar en equipo':'Hufflepuff',
        'Leer y aprender cosas nuevas':'Ravenclaw',
    },
    'answer_3':{
        'Defensa contra las artes oscuras':'Gryffindor',
        'Pociones':'Slytherin',
        'Cuidado de criaturas mágicas':'Hufflepuff',
        'Encantamientos':'Ravenclaw',
    },
    'answer_4':{
        'León':'Gryffindor',
        'Serpiente':'Slytherin',
        'Tejón':'Hufflepuff',
        'Águila':'Ravenclaw',
    },
    'answer_5':{
        'Valiente':'Gryffindor',
        'Astuto/a':'Slytherin',
        'Leal':'Hufflepuff',
        'Inteligente':'Ravenclaw',
    },
    'answer_6':{
        'Ser un héroe o heroína':'Gryffindor',
        'Ser poderoso/a y exitoso/a':'Slytherin',
        'Tener una vida plena y feliz':'Hufflepuff',
        'Ser conocido/a por tu sabiduría y conocimiento':'Ravenclaw',
    },
    'answer_7':{
        'Coraje':'Gryffindor',
        'Ambición':'Slytherin',
        'Paciencia':'Hufflepuff',
        'Creatividad':'Ravenclaw',
    },
    'answer_8':{
        'Un fénix':'Gryffindor',
        'Una serpiente':'Slytherin',
        'Un perro mágico':'Hufflepuff',
        'Un búho':'Ravenclaw',
    },
    'answer_9':{
        'Adivinación':'Ravenclaw',
        'Historia de la Magia':'Ravenclaw',
        'Herbología':'Hufflepuff',
        'Transformaciones':'Gryffindor',
    },
    'answer_10':{
        'La honestidad':'Hufflepuff',
        'La astucia':'Slytherin',
        'La amistad':'Gryffindor',
        'La inteligencia':'Ravenclaw',
    }
}

def check_input(expression_input):
    while True:
        number_input = input(expression_input)
        try:
            if int(number_input) > 0 and int(number_input) < 5:
                return number_input
            else:
                print('>>> Por favor, use los numeros del 1 al 4.\n')
        except:
            print('>>> Por favor, use los numeros del 1 al 4.\n')

def quizz(name):
    query_key = 'query_'
    answer_key = 'answer_'
    cont = 1
    player_responses = []
    
    for i in QUIZZ:
        query = f'>>> {QUIZZ[(query_key + str(cont))]}'
        answers = ANSWER[(answer_key + str(cont))]
        print('---------------------------------------------------------')
        print(query)
        for index, x in enumerate(answers.keys()):
            print(f'>>> {index + 1} - {x}')
        print('---------------------------------------------------------')
        player_input = check_input(f'>>> Inserta tú respuesta {name}\n')
        house = (answers[list(answers.keys())[int(player_input)-1]])
        player_responses.append(house)
        cont+=1

    return player_responses

def check_results_quizz(list_answer):
    from collections import Counter
    result = Counter(list_answer)

    return max(result, key=result.get)

if __name__ == '__main__':
    print('---------------------------------------------------------')
    print('Bienvenidos tod@s a la Ceremonia de Selección de Hogwarts')
    print('---------------------------------------------------------\n')
    time.sleep(0.5)
    print('>>> Que suba el siguiente aspirante, por favor.')
    time.sleep(0.5)
    name = input('>>> ¿Cuál es su nombre?\n')
    time.sleep(0.5)
    print(f'>>> Bueno {name} le dejo con el Sombrero Seleccionador, responda sus preguntas sin miedo.\n')
    time.sleep(0.5)
    print('---------------------------------------------------------\n')
    print(f'>>> Hola {name}, soy el Sombrero Seleccionador, empecemos con las preguntas.')
    print('>>> Para marcar su respuesta use los números 1, 2, 3 o 4\n')
    time.sleep(0.5)
    #name = 'Harry'
    answers = quizz(name)
    print(f'>>> {name} has terminado de responder las preguntas.\n')
    print(f'>>> Ahora es mi turno para decidir ...\n')
    time.sleep(1.5)
    result = check_results_quizz(answers)
    print(f'>>> Ehorabuena {name} has sido seleccionado para {result} !!\n')

