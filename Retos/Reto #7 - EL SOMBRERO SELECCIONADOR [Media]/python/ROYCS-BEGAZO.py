casas_puntos = {
    'Gryffindor':0,
    'Hufflepuff':0,
    'Ravenclaw':0,
    'Slytherin':0
}

banco_preguntas = [
    {
    'pregunta':'¿Que cualidad valoras mas?',
    'opciones':[
            ['a)Lealtad','b)Amabilidad','c)Pasion','d)Honor'],
            {
                'a':{'Gryffindor':2,'Hufflepuff':1},
                'b':{'Hufflepuff':2,'Gryffindor':1},
                'c':{'Slytherin':2,'Ravenclaw':1},
                'd':{'Ravenclaw':2,'Slytherin':1}
            }
        ],
},
{
'pregunta':'¿Si tu casa estuviera en llamas que salvarias',
    'opciones':[
            ['a)Libro de hechizos antiguo','b)Reliquia familiar',
            'c)Objeto de valor sentimental','d)Un objeti importante pero pesado'],
            {
                'd':{'Gryffindor':2,'Hufflepuff':1},
                'd':{'Hufflepuff':2,'Gryffindor':1},
                'b':{'Slytherin':2,'Ravenclaw':1},
                'a':{'Ravenclaw':2,'Slytherin':1}
            }
        ]
},
{
'pregunta':'¿Que materia escogerias?',
    'opciones':[
            ['a)Quiditch','b)Cuidado de animales fantasticos',
            'c)Encantamientos oscuros','d)Posiones Antiguas'],
            {
                'a':{'Gryffindor':2,'Hufflepuff':1},
                'b':{'Hufflepuff':2,'Gryffindor':1},
                'c':{'Slytherin':2,'Ravenclaw':1},
                'd':{'Ravenclaw':2,'Slytherin':1}
            }
        ]
},
{
'pregunta':'¿Que prefiriras obtener?',
    'opciones':[
            ['a)Hablar parsel','b)Memoria fotografica',
            'c)Entender a los animales','d)Una espada irrompible'],
            {
                'd':{'Gryffindor':2,'Hufflepuff':1},
                'c':{'Hufflepuff':2,'Gryffindor':1},
                'a':{'Slytherin':2,'Ravenclaw':1},
                'b':{'Ravenclaw':2,'Slytherin':1}
            }
        ]
},
{
'pregunta':'Un animal te sigue,¿Que es?',
    'opciones':[
            ['a)Un leon','b)Un panda','c)Un buho','d)Una serpiente'],
            {
                'a':{'Gryffindor':2,'Hufflepuff':1},
                'b':{'Hufflepuff':2,'Gryffindor':1},
                'c':{'Slytherin':2,'Ravenclaw':1},
                'd':{'Ravenclaw':2,'Slytherin':1}
            }
        ]
}
]

for i in range(len(banco_preguntas)):
    print(banco_preguntas[i]['pregunta'])
    for o in banco_preguntas[i]['opciones'][0]:
        print(o)
    opc = input('ingrese la letra de la opcion ').lower()
    while True:
        if opc not in ('a','b','c','d'):
            print('alternativa no valida')
            opc = input('ingrese la letra de la opcion ').lower()
        else:
            break
    for casa, puntos in banco_preguntas[i]['opciones'][1][opc].items():
        casas_puntos[casa] += puntos
winner = max(casas_puntos, key=casas_puntos.get)
print(f'tu casa escogida es.......{winner}¡')





