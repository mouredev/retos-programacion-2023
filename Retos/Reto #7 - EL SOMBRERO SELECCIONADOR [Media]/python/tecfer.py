'''
 Crea un programa que simule el comportamiento del sombrero selccionador del
 universo mágico de Harry Potter.
 - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
  coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
  Por ejemplo, en Slytherin se premia la ambición y la astucia.

Las respuestas están ordenadas por casa, Gryffindor, Slytherin , Hufflepuff y Ravenclaw. 
Se va incrementando un contador y se selecciona por número de "votos", en caso de empate permanece 
la primera en el diccionario.
'''

textos = {  '1':{
            'pregunta':'¿Qué cualidad valoras más en un amigo?',
            '1':'La valentía',
            '2':'La astucia',
            '3':'La sabiduría',
            '4':'La lealtad'},
            '2':{
            'pregunta':'¿Qué asignatura te resulta más interesante?',
            '1':'Defensa contra las Artes Oscuras',
            '2':'Pociones',
            '3':'Astronomía',
            '4':'Herbología'},
            '3':{
            'pregunta':'¿Qué tipo de tarea te resulta más satisfactoria?',
            '1':'Superar tus propios límites',
            '2':'Vencer a tus oponentes',
            '3':'Descubrir nuevos conocimientos',
            '4':'Ayudar a los demás'},
            '4':{
            'pregunta':'¿Qué lugar te gustaría explorar en Hogwarts?',
            '1':'La Sala de los Menesteres',
            '2':'Las Mazmorras',
            '3':'La Biblioteca',
            '4':'El Invernadero'},
            '5':{
            'pregunta':'¿Qué te motiva a seguir adelante?',
            '1':'La búsqueda de aventura',
            '2':'La búsqueda de poder',
            '3':'La búsqueda del conocimiento',
            '4':'La búsqueda de la felicidad'}
        }
        
casas = {   1:{'nombre':'Gryffindor','puntos':0},
            2:{'nombre':'Slytherin','puntos':0},
            3:{'nombre':'Hufflepuff','puntos':0},
            4:{'nombre':'Ravenclaw','puntos':0}}  

for num_pregunta, txt in textos.items():

    respuesta =0
    
    while (respuesta==0):
        
        print(f"\n\n\nPregunta {num_pregunta}: {txt['pregunta']}")
        print(f"\t1. {txt['1']}")
        print(f"\t2. {txt['2']}")
        print(f"\t3. {txt['3']}")
        print(f"\t4. {txt['4']}")
        respuesta = input("Respuesta: ")
        if respuesta.isdigit():
            respuesta=int(respuesta)
            
        else:
            respuesta=0
        
        if (respuesta>0) and (respuesta<5):
            casas[respuesta]['puntos']+=1
            
        else:
            respuesta=0
            print("\nEsta respuesta no es válida\n")

mayor_puntuacion = 0
for i in range(1,5):
    
    if mayor_puntuacion < casas[i]['puntos']:
        mayor_puntuacion = casas[i]['puntos']
        casa = casas[i]['nombre']

print(f"\n\n*** Perteneces a la casa {casa} ***")
