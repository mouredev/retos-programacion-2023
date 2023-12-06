# * Crea un programa que simule el comportamiento del sombrero selccionador del
# * universo mágico de Harry Potter.
# * - De ser posible realizará 5 preguntas(como mínimo) a través de la terminal.
# * - Cada pregunta tendrá 4 respuestas posibles(también a selecciona una a través de terminal).
# * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
# *   coloque al alumno en una de las 4 casas de Hogwarts(Gryffindor, Slytherin, Hufflepuff y Ravenclaw)
# * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
# *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
# */

from functools import reduce

#Clase que reperesenta una pregunta y sus respuestas

class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers


# Equipos de fútbol posibles
teams = {
         1: 'Granada CF',
         2: 'Real Madrid',
         3: 'Farsa, el equipo de los culerdos',
         4: 'Celtic de Pulianas'
}


# Array de preguntas y respuestas con sus puntos correspondientes a cada equipo
questions = [Question("Se acerca la fecha del próximo partido de tu equipo, ¿cómo te sientes?",
            [
            {"answer": 'Nervioso/a, todos los partidos de mi equipo los siento con pasión.', "points": [{"name": "Celtic", "points": 10}, {
                "name": "Farsa", "points": 0}, {"name": "GranadaCF", "points": 9}, {"name": "RMadrid", "points": 2}]},
            {"answer": 'No es relevante, cuando llegue la hora ya me sentaré a verlo tranquilamente.', 'points': [{'name': 'Celtic', 'points': 0}, {
                "name": "Farsa", "points": 7}, {"name": "GranadaCF", "points": 2}, {'name': 'RMadrid' ,'points': 7}]},
            {"answer": 'Los vecinos hablan sobre el partido los días previos, se nota el ambiente en la calle.', 'points': [
                {'name': 'Celtic', 'points': 4}, {'name': 'Farsa', 'points': 10}, {'name': 'GranadaCF', 'points': 1}, {'name': 'RMadrid', 'points': 9}]},
            {'answer': 'No como ni duermo los días previos de los nervios. Da igual que sean dieciseisavos de Copa o la última jornada de Liga, lo vivo.', 'points': [
                {'name': 'Celtic', 'points': 8}, {'name': 'Farsa', 'points': 1}, {'name': 'GranadaCF', 'points': 10}, {'name': 'RMadrid', 'points': 0}]}
            ]),

            Question("Estás en un bar y te das cuenta de que nadie es del mismo equipo que tú, ¿qué piensas?",
             [

                {'answer': 'Joder, mira que es raro.',
                 'points': [
                    {'name': 'Celtic', 'points': 10}, {'name': 'Farsa', 'points': 0}, {'name': 'GranadaCF', 'points': 3}, {'name': 'RMadrid', 'points': 2}
                ]},
                {'answer': 'Ya está esto lleno de borregos, míralos, todos viendo el Chirincirco.',
                 'points': [
                    {'name': 'Celtic', 'points': 1}, {'name': 'Farsa', 'points': 7}, {'name': 'GranadaCF', 'points': 4}, {'name': 'RMadrid', 'points': 9}
                ]},
                {'answer': 'Normal, si somos 4 gatos. Eh, pero con orgullo, coño.',
                  'points':[
                    {'name': 'Celtic', 'points': 7},
                    {'name': 'Farsa', 'points': 2},
                    {'name': 'GranadaCF', 'points': 10},
                    {'name': 'RMadrid', 'points': 2}
                ]},
                {'answer': 'Ups, igual tenía que haber ido al de dos calles más abajo...',
                 'points': [
                    {'name': 'Celtic', 'points': 10},
                    {'name': 'Farsa', 'points': 1},
                    {'name': 'GranadaCF', 'points': 8},
                      {'name': 'RMadrid', 'points': 1}]}
            ]),
            Question('Penalti a favor del Madrid/Barcelona. En la repetición se ve que no era. ¿Cómo reaccionas?',
             [

                 {'answer': 'Ya están robando estos perros.', 'points': [{'name': 'Celtic', 'points': 10}, {
                     'name': 'Farsa', 'points': 0}, {'name': 'GranadaCF', 'points': 9}, {'name': 'RMadrid', 'points': 2}]},
                 {'answer': 'Esto es una puta vergüenza! Soy el entrenador y los saco del campo, que se rían de su madre.', 'points': [
                     {'name': 'Celtic', 'points': 3}, {'name': 'Farsa', 'points': 10}, {'name': 'GranadaCF', 'points': 3}, {'name': 'RMadrid', 'points': 9}]},
                 {'answer': 'Ya la tenemos liada, ahora a aguantar a la prensa toda la semana...', 'points': [{'name': 'Celtic', 'points': 4}, {
                     'name': 'Farsa', 'points': 0}, {'name': 'GranadaCF','points': 9}, {'name': 'RMadrid', 'points': 2}]},
                 {'answer': 'Ya estamos con la prensa mamadora del movimiento', 'points': [{'name': 'Celtic', 'points': 10}, {
                     'name': 'Farsa', 'points': 0}, {'name': 'GranadaCF', 'points': 9}, {'name': 'RMadrid', 'points': 2}]}

             ]),
             Question('Caso contrario: última jornada de liga y una victoria de tu equipo hace que supere el objetivo marcado al principio del año.',
            [
             {'answer': 'Coño, coño, coño, coño, coño, coño. Como les dé por ganar me desnudo en la fuente del pueblo.', 'points': [
                 {'name': 'Celtic', 'points': 10}, {'name': 'Farsa', 'points': 0}, {'name': 'GranadaCF', 'points': 9}, {'name': 'RMadrid', 'points': 2}]},
             {'answer': 'Yaya, enséñame unos rezos de esos, que es para una cosa del finde.', 'points': [{'name': 'Celtic', 'points': 1}, {
                 'name': 'Farsa', 'points': 9}, {'name': 'GranadaCF', 'points': 2}, {'name': 'RMadrid', 'points': 6}]},
             {'answer': 'Pase lo que pase ha sido un temporadón, ¡qué orgullo de equipo!', 'points': [{'name': 'Celtic', 'points': 6}, {
                 'name': 'Farsa', 'points': 5}, {'name': 'GranadaCF', 'points': 4}, {'name': 'RMadrid', 'points': 4}]},
             {'answer': 'Con lo bien que vivía yo cuando éramos mediocres, qué ganas de matarnos con los nervios.', 'points': [
                 {'name': 'Celtic', 'points': 10}, {'name': 'Farsa', 'points': 1}, {'name': 'GranadaCF', 'points': 9}, {'name': 'RMadrid', 'points': 4}]},
         ]),
         Question('Final de la temporada, tu equipo desciende a Segunda División. Vaya veranito te vas a pegar...',
         [
             {'answer': 'JAJAJAJAJAJAJAJAJA EN SEGUNDA DICE, ¡QUE SOY DEL MADRID/BARÇA, TOLAI!', 'points': [{'name': 'Celtic', 'points': 0}, {
                 'name': 'Farsa', 'points': 10}, {'name': 'GranadaCF', 'points': 0}, {'name': 'RMadrid', 'points': 10}]},
             {'answer': 'Lloro, me enfado, durante las primeras semanas va a ser una auténtica pesadilla. No puede pasarnos a nosotros...', 'points': [
                 {'name': 'Celtic', 'points': 5}, {'name': 'Farsa', 'points': 7}, {'name': 'GranadaCF', 'points': 3}, {'name': 'RMadrid', 'points': 4}]},
             {'answer': 'No pudo ser, nos vino grande la categoría. Volveremos con más fuerza, ¡seguro!', 'points': [
                 {'name': 'Celtic', 'points': 7}, {'name': 'Farsa', 'points': 2}, {'name': 'GranadaCF', 'points': 9}, {'name': 'RMadrid', 'points': 2}]},
             {'answer': 'Otra vez al hoyo. El año que viene mi abono se lo pueden meter por el...', 'points': [{'name': 'Celtic', 'points': 4}, {
                 'name': 'Farsa', 'points': 0}, {'name': 'GranadaCF', 'points': 9}, {'name': 'RMadrid', 'points': 0}]},
         ])
]

# Equipos participantes en el quiz
teams = {
    'Celtic': {'name': 'Celtic de Pulianas', 'points': 0},
    'Farsa': {'name': 'Farsa', 'points': 0},
    'GranadaCF': {'name': 'Granada CF', 'points': 0},
    'RMadrid': {'name': 'Real Madrid', 'points': 0}
}


#Funcion que devuelve de que equipo eres
def your_team_is():
    team = reduce(lambda x, y: x if teams[x]['points'] > teams[y]['points'] else y, teams.keys())
    return teams[team]['name']

#Funcion que realiza una pregunta y devuelve la respuesta
def get_answer():
    answer = input("Introduce una respuesta (1, 2, 3 o 4):")
    if answer not in ['1', '2', '3', '4']:
        print("Respuesta incorrecta")
        return get_answer()
    return answer


#Funcion que suma los puntos a los equipos
def add_points(points):
    for point in points:
        teams[point['name']]['points'] += point['points']


#Funcion que realiza el quiz y devuelve el equipo al que perteneces
def quiz():

    print('\nBienvenido al test de fútbol. Responde a las siguientes preguntas y averigua qué equipo eres:\n')
    for question in questions:
        print(question.question)
        print("")
        i=1
        for answer in question.answers:
            print("{}. {}".format(i, answer['answer']))
            i += 1
        response = get_answer()

        points = question.answers[int(response) - 1]['points']
        add_points(points)

    print("\nEnhorabuena!! Tu equipo es: {}".format(your_team_is()))



#Llamada a la funcion
quiz()

