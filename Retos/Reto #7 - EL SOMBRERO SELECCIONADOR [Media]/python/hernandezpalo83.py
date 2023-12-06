#
 # Crea un programa que simule el comportamiento del sombrero selccionador del
 # universo mágico de Harry Potter.
 # - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 # - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 # - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 #   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 # - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 #   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 #
# Caracteristicas: 
# La Casa de Gryffindor valora el coraje por encima de todo, pero también la osadía, el temple y la caballerosidad. 
#                       Sus estudiantes son valientes, pero también muy imprudentes.
# La Casa de Hufflepuff se caracteriza por valorar la capacidad de trabajo, con estudiantes amigables y leales. 
#                       Los estudiantes de esta casa son conocidos por ser trabajadores, amigables, leales y sin prejuicios
# La Casa Ravenclaw valora el aprendizaje, la sabiduría, el ingenio, y el intelecto como elementos importantes para formar parte de su casa. 
#                       Al ser magos de mucho talento, Hermione Granger estuvo a punto de ser seleccionada por Ravenclaw.
# La Casa Slytherin cuenta con miembros ambiciosos, inteligentes, muy astutos y que tienden a ser líderes fuertes. 
#                       Aunque también son unos supervivientes, lo que les hace pensar antes de actuar (al contrario que los Gryffindor), pese a tener un claro desprecio por las reglas.

casas = {
    "1":"Gryffindor",
    "2":"Huffplepuff",
    "3":"Slytherin",
    "4":"Ravenclaw"
}

preguntas = [
    {
        "pregunta":"1. ¿Que palabra te describe mejor?",
        "respuesta":[
            "1) Osadia",
            "2) Curiosidad",
            "3) Ambición",
            "4) Lealtad"
        ]
    },
    {
        "pregunta":"2. ¿Qué opinas de los muggles?",
        "respuesta":[
            "1) Están bien es su mundo",
            "2) Me dan igual",
            "3) No deberian existir",
            "4) Somo superiores a ellos"
        ]
    },
    {
        "pregunta":"3. ¿Le temes al Señor Oscuro?",
        "respuesta":[
            "1) No, hay que defendernos de el",
            "2) Si, me da mucho miedo",
            "3) Si, por eso hay que hacer lo que diga",
            "4) No, pero no me enfrentaria a el"
        ]
    },
    {
        "pregunta":"4. ¿A cuál de estos personajes admiras?",
        "respuesta":[
            "1) Minerca McGonagall",
            "2) Cedric Diggory",
            "3) Severus Snape",
            "4) Alastor Moody"
        ]
    },
    {
        "pregunta":"5. ¿Qué actividad habrías preferido hacer en tu estancia en la escuela?",
        "respuesta":[
            "1) Estar en el equipo de Quidditch",
            "2) La clase de herbologia",
            "3) Hacer bromas a los profesores",
            "4) Leer en la bibioteca"
        ]
    }
]

respuesta_casa = {"1":0, "2":0, "3":0, "4":0}

def hacer_pregunta(pregunta):
    valid = False
    while not valid:
        print(f'\n{pregunta["pregunta"]}')
        for alternativa in pregunta["respuesta"]:
            print(alternativa)
        r = input("¿Cual es su respuesta? ")
        if r not in respuesta_casa:
            valid = False
            print( "Opción no valida. Por favor seleccione una de las siguientes opciones ( 1, 2, 3, 4)")
        else:
            valid = True
    respuesta_casa[r] += 1
    return valid

print("\n\n\nBinvenido a Hogwarts!\
    \n---------------------------------\
    \n ¿Eres valiente, ambicioso, leal o sabio? ¿A qué casa de Hogwarts perteneces?\
    \n\
    \n ¡No tengas miedo! ¡Y no recibirás una bofetada! \
    \n Estás en buenas manos (aunque yo no las tenga). \
    \n\
    \n El sombrero seleccionardor se encargará de seleccionar tu casa de Hogwarts\
    \n--------------------------------------------------------------------------")

for pregunta in preguntas:
    r_valida = hacer_pregunta(pregunta)        

# He decidido la puntuación se define por el que mas respuestas tenga de esa casa.
puntos = max(respuesta_casa, key=respuesta_casa.get)
casa_final = casas[puntos].upper()

print(f"\n\n\nVamos a ver tus respuestas!\
    \n---------------------------------\
    \n ¿Eres valiente, ambicioso, leal o sabio? ¿A qué casa de Hogwarts perteneces?\
    \n\
    \n Mmm..................... Dificil decision la que me depara\
    \n Eres de la casa {casa_final}!\
    \n--------------------------------------------------------------------------")

