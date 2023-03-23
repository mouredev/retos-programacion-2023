import random

class pregunta:
    def __init__(self,pregunta, respuestas):
        self.pregunta=pregunta
        self.respuestas=respuestas

def combrobar_respuesta():
    answer=input('Escoge a, b, c o d\n')
    if answer == 'a' or  answer == 'b' or answer == 'c' or answer == 'd':
        return answer
    return combrobar_respuesta()

def sombrero_seleccionador():
    
    #Gryffindor - valentia y disposicion
    #Slytherin - ambicion y astucia
    #Hufflepuff - lealtad y honestidad
    #Ravenclaw - creatividad y curiosidad

    hat_questions=[pregunta('¿Cómo te definirias?',[('a. Valiente','Gryffindor'),
                                                   ('b. Astuto', 'Slytherin'),
                                                   ('c. Leal', 'Hufflepuff'),
                                                   ('d. Curioso','Ravenclaw')]),
                  
                  pregunta('¿Cuál es tu clase favorita?',[('a. Vuelo','Gryffindor'),
                                                          ('b. Pociones','Hufflepuff'),
                                                          ('c. Defensa contra las artes oscuras','Ravenclaw'),
                                                          ('d. Animales fantásticos','Slytherin')]),

                  pregunta('¿Qué tipo de instrumento agrada mas a tu oído?',[('a. Violin','Slytherin'),
                                                                             ('b. Tambores','Hufflepuff'),
                                                                             ('c. Piano','Ravenclaw'),
                                                                             ('d. Trompeta','Gryffindor')]),

                  pregunta('¿Cuál de las siguientes opciones le resulta más difícil de manejar?',[('a. Hambre','Ravenclaw'),
                                                                                                  ('b. Frio','Gryffindor'),
                                                                                                  ('c. Soledad','Slytherin'),
                                                                                                  ('d. Aburrimiento','Hufflepuff')]),

                  pregunta('Si pudieras tener algún poder, ¿cuál elegirías?',[('a. El poder de leer la mente','Hufflepuff'),
                                                                               ('b. El poder de la invisibilidad','Ravenclaw'),
                                                                               ('c. El poder de la fuerza sobrehumana','Gryffindor'),
                                                                               ('d. El poder de cambiar tu apariencia a voluntad','Slytherin')])]
    
    houses={'Gryffindor':0,'Slytherin':0,'Hufflepuff':0,'Ravenclaw':0}

    for question in hat_questions: 
        print(question.pregunta)
        for respuesta in question.respuestas:
            print(respuesta[0])
        answer=combrobar_respuesta()
        if answer == 'a':
            houses[(question.respuestas[0][1])]+=1
        elif answer == 'b':
            houses[(question.respuestas[1][1])]+=1
        elif answer == 'c':
            houses[(question.respuestas[2][1])]+=1
        elif answer == 'd':
            houses[(question.respuestas[3][1])]+=1
    
    casa_final=[]
    max_points=0

    for house, points in houses.items():
        if points>max_points:
            casa_final.clear()
            casa_final.append(house)
            max_points=points
        elif max_points==points:
            casa_final.append(house)
    
    print(houses)

    if len(casa_final)>1:
        print(f"No ha estado claro, pero te enviaré a... ¡{random.choice(casa_final)}!")
    else:
        print(f"Definitivamente perteneces a... ¡{casa_final[0]}!")

sombrero_seleccionador()