questions = [
    {
        'question': 'Cual de los siguientes animales te gusta mas?',
        'options': {
            1: 'Aguila',
            2: 'Liebre',
            3: 'Pulpo',
            4: 'Panda'
        },
        'answer': 0
    },
    {
        'question': 'Cual de los siguientes colores te gusta mas?',
        'options': {
            1: 'Verde',
            2: 'Rojo',
            3: 'Azul',
            4: 'Rosa'
        },
        'answer': 0
    },
    {
        'question': 'Cual de las siguientes actividades te gusta mas?',
        'options': {
            1: 'Ir a un parque de diversiones',
            2: 'Ver una pelicula',
            3: 'Leer un libro',
            4: 'Hacer un picnic'
        },
        'answer': 0
    },
    {
        'question': 'Donde preferirias estar?',
        'options': {
            1: 'Un rascacielos',
            2: 'Un barco',
            3: 'Un museo',
            4: 'Un jardin'
        },
        'answer': 0
    },
    {
        'question': 'Que epoca del año te gusta mas?',
        'options': {
            1: 'Halloween',
            2: 'Navidad',
            3: 'Dia del padre/madre',
            4: 'San Valentin'
        },
        'answer': 0
    },
]

houses = [
    {
        'house': 'Slytherin',
        'points': 0
    },
    {
        'house': 'Griffindor',
        'points': 0
    },
    {
        'house': 'Ravenclaw',
        'points': 0
    },
    {
        'house': 'Hufflepuf',
        'points': 0
    }
]

for question in questions:
    print(question['question'])
    print(question['options'])

    validation = False

    while not validation:
        ans = int(input('Ingresa un número para responder:'))

        if 1 <= ans <= 4:
            question['answer'] = ans
            validation = True
        else:
            print('Ingresa una respuesta valida')

for question in questions:
    if question['answer'] == 1:
        houses[0]['points'] += 1
    if question['answer'] == 2:
        houses[1]['points'] += 1
    if question['answer'] == 3:
        houses[2]['points'] += 1
    if question['answer'] == 4:
        houses[3]['points'] += 1

max = 0
usr_house = ''

for house in houses:
    if house['points'] > max:
        max = house['points']
        usr_house = house['house']

print(f'Felicidades! Perteneces a {usr_house} con una afinidad de {max}')