puntos = {
    'gryffindor': 0,
    'slytherin': 0,
    'hufflepuff': 0,
    'ravenclaw': 0
}

ans = []

def run_me(input,question):
    if question == 0:
        if input == 3:
            puntos['gryffindor'] += 1
        if input == 2:
            puntos['slytherin'] += 1
        if input == 1:
            puntos['hufflepuff'] += 1
        if input == 4:
            puntos['ravenclaw'] += 1
    if question == 1:
        if input == 1:
            puntos['gryffindor'] += 1
        if input == 3:
            puntos['slytherin'] += 1
        if input == 2:
            puntos['hufflepuff'] += 1
        if input == 4:
            puntos['ravenclaw'] += 1
    if question == 2:
        if input == 2:
            puntos['gryffindor'] += 1
        if input == 4:
            puntos['slytherin'] += 1
        if input == 3:
            puntos['hufflepuff'] += 1
        if input == 1:
            puntos['ravenclaw'] += 1
    if question == 3:
        if input == 4:
            puntos['gryffindor'] += 1
        if input == 1:
            puntos['slytherin'] += 1
        if input == 3:
            puntos['hufflepuff'] += 1
        if input == 2:
            puntos['ravenclaw'] += 1
    if question == 4:
        if input == 1:
            puntos['gryffindor'] += 1
        if input == 3:
            puntos['slytherin'] += 1
        if input == 4:
            puntos['hufflepuff'] += 1
        if input == 2:
            puntos['ravenclaw'] += 1

arr = ['¿Qué característica te describe mejor?', 
        'Tu amigo tiene un problema; ¡Lo están acosando! ¿Qué haces?',
        '¿Cuál sería la mejor mascota del mundo?',
        'Si ves un cartel que dice "no entrar - ¡Peligro! ¡Peligro!", ¿Qué harías?',
        '¿Cuál diría tu familia que es tu peor característica?'
    ]
counter = 0

while counter < 4:
    try:
        print(f'{counter+1} - {arr[counter]}')
        if counter == 0:
            resp = int(input('\t1) leal 2) astuto 3) valiente 4) inteligente\n'))
        if counter == 1:
            resp = int(input('\t1) ¡Meterme sin  pensar y defenderlo! 2) Rápidamente formular un plan para ayudar 3) Consider cuidadosamente… ¿Cómo me puedo beneficiar de esta situación? 4) Buscar un profesor; alguno podrá ayudar más que vos\n'))
        if counter == 2:
            resp = int(input('\t1) Un buho o un fénix; que sea inteligente 2) Un hipogrifo: feroz, rápido e intrépido 3) Un gato o perro: leal y amable 4) Una serpiente o lagarto\n'))
        if counter == 3:
            resp = int(input('\t1) Reirme del cartel y entregar. Como si fuera que alguien o algo me pueda llegar a decir qué puedo hacer 2) Marcharme. Rápidamente y no mirar atrás 3) Dejarlo en su lugar. Tiene que haber una buena razón para el cartel 4) ¡Entrar! Si están ahuyentando a la gente es porque hay algo increíble\n'))
        if counter == 4:
            resp = int(input('\t1) Imprudente - no pienso antes de actuar 2) Un sabelotodo 3) ¿Peor qué? No tengo malas cualidades 4) Soy demasiado amable\n'))
        if resp > 4 or resp < 1:
            print('¡Las respuestas tienen que ser entre 1 y 4!\n')
            pass
        else:
            ans.append(resp)
            counter += 1
    except ValueError:
        print("Oops! Solo números del 1 al 4...")
    except KeyboardInterrupt:
        print('Saliendo de la ejecución...')
        exit()

counter = 0
for i in ans:
    run_me(i,counter)
    counter += 1

print(puntos)
print(max(puntos,key=puntos.get))
