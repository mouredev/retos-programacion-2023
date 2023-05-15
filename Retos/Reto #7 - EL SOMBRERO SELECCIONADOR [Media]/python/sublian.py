"""Reto #7: El sombrero seleccionador
#### Dificultad: Media | Publicación: 13/02/23 | Corrección: 20/02/23

## Enunciado

 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
"""
#Gryffindor:    valor
#Slytherin:     ambicion
#Hufflepuff:    sabiduria
#Ravenclaw:     lealtad
import random

class HatQuestion:
    def __init__(self, question, answer):
        self.question=question
        self.answer=answer

#obtiene y valida la respuesta recibida
def get_answer():                
    answer=input("Responde [1-4]: ")
    if answer in ["1","2","3","4"]:
        return int(answer)
    return get_answer()
    
#listado de preguntas con respuestas        
hat_questions=[HatQuestion("¿Como te definirias?", [
                            ("1. Valiente", "Gryffindor"),
                            ("2. Leal", "Hufflepuff"),
                            ("3. Sabio", "Ravenclaw"),
                            ("4. Ambicioso", "Slytherin")]),
                HatQuestion("¿Cual es tu clase favorita?", [
                            ("1. Vuelo", "Gryffindor"),
                            ("2. Pociones", "Ravenclaw"),
                            ("3. Defensa contra las artes oscuras", "Slytherin"),
                            ("4. Animales fantasticos", "Hufflepuff")]),
                HatQuestion("Dada la opción, preferirías inventar una poción que garantizara:", [
                            ("1. Gloria", "Gryffindor"),
                            ("2. Poder", "Slytherin"),
                            ("3. Sabiduria", "Ravenclaw"),
                            ("4. Amor", "Hufflepuff")]),
                HatQuestion("Cual prefirias ser:", [
                            ("1. Temido", "Slytherin"),
                            ("2. Elogiado", "Gryffindor"),
                            ("3. Imitado", "Ravenclaw"),
                            ("4. Confiable", "Hufflepuff")]),
                HatQuestion("Curioso. siento algo en ti. Algún rasgo de carácter... hmm... ¿cuál?", [
                            ("1. Valor", "Gryffindor"),
                            ("2. Lealtad", "Hufflepuff"),
                            ("3. Curiosidad", "Ravenclaw"),
                            ("4. Ambicion", "Slytherin")])]        

#diccionario de casas
houses={"Gryffindor":0,    
        "Slytherin":0,
        "Hufflepuff":0,
        "Ravenclaw":0}     

#barajeo las preguntas con sus respuestas
random.shuffle(hat_questions)

#muestro la informacion y recibo respuestas
print("Empieza el test del Sombrero Seleccionador, averigua a qué casa de Hogwarts perteneces!")
for hat_question in hat_questions:    
    print(hat_question.question)
    for hat_answer in hat_question.answer:
        print(hat_answer[0])
    house = hat_question.answer[get_answer()-1][1]
    houses[house]+=1       

#valido la informacion para seleccionar la casa de magia con mas puntos
selected_house=[]
max_point=0
for house, points in houses.items():
    if points>max_point:
        selected_house.clear()
        selected_house.append(house)        
        max_point=points
    elif points==max_point:
        selected_house.append(house)
        max_point=points

#seccion de validacion que informa si hay una casa ganadora o se elige al azar en caso de empate
if len(selected_house)==1:
    print(f"\nLo tengo claro... ¡{selected_house[0].capitalize()}!")
else:
    print(f"\nTe recomendamos... ¡{random.choice(selected_house).capitalize()}!")