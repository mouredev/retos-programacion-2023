'''
    Crea un programa que simule el comportamiento del sombrero selccionador del
    universo mágico de Harry Potter.
    - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
    - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
        coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
    - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
        Por ejemplo, en Slytherin se premia la ambición y la astucia.
'''

def elige_casa():
    
    preguntas = ['¿Qué cualidad valoras más en ti mismo?',
                 '¿Qué harías si te enfrentas a un troll?',
                 '¿Cuál es tu hechizo favorito?',
                 '¿Qué color te atrae más?',
                 '¿Qué criatura mágica te gustaría tener como mascota?']
    
    respuestas = [['A. Coraje', 'B. Inteligencia', 'C. Lealtad', 'D. Astucia'],
                  ['A. Huir', 'B. Atacar', 'C. Pedir ayuda', 'D. Intentar razonar con él'],
                  ['A. Expecto Patronum', 'B. Wingardium Leviosa', 'D. Expelliarmus', 'D. Lumos'],
                  ['A. Rojo', 'B. Azul', 'C. Amarillo', 'D. Verde'],
                  ['A. Búho', 'B. Gato', 'C. Rata', 'D. Lechuza']]
    
    respuesta = []
    puntuaciones = {'Gryffindor': 0,
                    'Ravenclaw': 0,
                    'Hufflepuff': 0,
                    'Slythering': 0}
    
    for i in range(len(preguntas)):
        print(preguntas[i])
        for j in respuestas[i]:
            print(j)
        respuesta = input('Elige una de las respuestas (a, b, c, d): ')
        respuestas.append(respuesta)
        
    for i in respuestas:
        puntuaciones['Gryffindor'] += 1 if i == 'A' else 0
        puntuaciones['Ravenclaw'] += 1 if i == 'B' else 0
        puntuaciones['Hufflepuff'] += 1 if i == 'C' else 0
        puntuaciones['Slythering'] += 1 if i == 'D' else 0

    casa = max(puntuaciones, key = puntuaciones.get)
    return casa    
        
if __name__ == '__main__':
    print('Selecciono tu casa en base a tus respuestas...\n')
    print(f"Tu casa es...' {elige_casa()}")