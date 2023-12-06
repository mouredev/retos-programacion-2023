"""
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
"""
import random                   #importo random para usar en la función *pregunta_el_sombrero* y que lance una pregunta al azar
""" ------------------------------------------------------------------------------------------------------ """
def tu_nombre():                #En esta función preguntamos el nombre del proto-mago y evitamos que quede vacío atrapándolo con un while
    nombre_mago=input("Hola, joven. ¿Cuál es tu nombre?")
    while nombre_mago == "" :
        nombre_mago=input("Caray! Veo que eres tímido. ¿Me puedes decir tu nombre?")
    return nombre_mago
""" ------------------------------------------------------------------------------------------------------ """
def pregunta_el_sombrero():     #la idea es que esta función sea un colector de preguntas y las suelte random
    preguntas={ 1:"¿Cuál es el rasgo que más destaca de tu personalidad?",
                2:"Si fueras un dulce Bertie Botts, ¿Qué sabor serías? ",
                3:"¿Cuál es tu mayor miedo?",
                4:"Hay un troll en las mazmorras, ¿Qué haces?",
                5:"¿Qué es lo que más anhelas aprender en Hogwarts?",
                6:"Si pudieras tener algún poder, ¿cuál elegirías?",
                7:"¿Cuál es tu bebida favorita?",
                8:"¿Cuál preferirías de mascota?",
                9:"Un muggle se enfrenta a ti. ¿Qué haces?"}
    respuestas_multiples={ 1:"1. Fuerte y veloz\n2. Gran conversador\n3. Ingenio para resolver cualquier problema\n4. Soy superior a los demás\n",
                2:"1. Me gustan todos\n2. Manzana verde y malvavisco\n3. Salchipapa y cerumen de oídos\n4. Todos saben a huevo podrido\n",
                3:"1. Las Arañas\n2. Perder un amigo\n3. Los necromagos\n4. Los asquerosos sangresucia\n",
                4:"1. Me enfrento a él\n2. Busco a un precepto\n3. Me hago el muerto\n4. Me meo\n",
                5:"1. Volar en una escoba\n2. Criaturas mágicas\n3. Pociones\n4. Maleficios y hechizos\n",
                6:"1. Fuerza sobrehumana\n2. La invisibilidad\n3. Leer la mente\n4. Manipular el tiempo\n",
                7:"1. Cerveza de mantequilla\n2. Zumo de Calabaza\n3. Vino de saúco\n4. Agua del grifo\n",
                8:"1. Lechuza\n2. Armiño\n3. Cuervo\n4. Serpiente\n",
                9:"1. Petrificus Totalus\n2. Wingardium Leviosa\n3. Mimble Wimble\n4. Avada Kedavra\n"}
    random_preg=random.randint(1, len(preguntas))           #lo optimo sería que no se repitan las preguntas, pero otro día será
    print(preguntas[random_preg])                           #preguntas elegida por random_preg
    print(respuestas_multiples[random_preg])                #respuesta correspondiente con el mismo index   
                                                            #Se podría meter todo en un mismo diccionario
    respuesta=""
    while respuesta != "1" and respuesta != "2" and respuesta != "3" and respuesta != "4":
        respuesta = input("Escoge una opción: ")            #evito que meta valores distintos de las opciones habilitadas 1,2,3,4
    return int(respuesta)                                   #devuelve como entero los puntos o con la clave de la casa
""" ------------------------------------------------------------------------------------------------------ """
def comprueba_empate(valores_casas):                        #con esta funcion se busca deshacer empates
    lista_puntos=[] 
    for i in valores_casas:                                 #buscamos los valores de seleccion tomados en cada pregunta
        item=valores_casas.get(i)
        lista_puntos.append(item[0])
    lista_puntos=sorted(lista_puntos, reverse=True)         #se ordenan
    lista_puntos.pop()                                      #se borran los más bajos    
    lista_puntos.pop()
    if len(set(lista_puntos)) != 2:                         #con set compruebo que los valores no se repiten
        return True
    else:
        return False
""" ------------------------------------------------------------------------------------------------------ """
def sistema_puntos_superpop(puntos_pop): #Con el sistema de puntuación de la superpop, cada CASA tiene un rango de puntos asociado en función del valor de cada respuesta
    # print(f"Tiente {puntos_pop}, veamos a que casa te asociamos")
    if puntos_pop<=5:           
        print("\n\nHas sido audaz y valiente en tus respuestas.\n¡¡Bienvenido a Gryffindor!!")
    elif puntos_pop<=10:
        print("\n\nHas sido leal y paciente con tus compañeros.\n¡¡Serás uno más en Hufflepuff!!")
    elif puntos_pop<=15:
        print("\n\nHas sido inteligente y creativo resolviendo enigmas.\n¡¡Despierta tu intelecto en Ravenclaw!!")
    else:
        print("\n\nHas sido ambicioso y astuto para salir ileso de estos entuertos.\n¡¡Vigila tu espalda en Slytherin!!")
""" ------------------------------------------------------------------------------------------------------ """
def sistema_puntos_por_casa(evalua_casas):
    casa_compatible=max(evalua_casas)
    casa_compatible=casa_compatible.pop(1)
    print(f"Has sido seleccionado como un nuevo miembro de {casa_compatible}")
""" ------------------------------------------------------------------------------------------------------ """
def sombrero_howarts(alumno):                               #tenemos el nombre del mago y comenzamos el cuestionario del sombrero.
    print(f"\nHola, {alumno}. Como nuevo alumno de esta escuela, debemos buscar una casa en Howarts para ti.\nPreguntemos al Sombrero Seleccionador en que casa te ubicamos.")
    print("El Sombrero te hará unas preguntas, así que responde sabiamente. Comencemos:\n")
    puntuacion, preguntas, empate=0, 0, True               #inicio variables de control y un dict para guardar valores
    casas={1:[0,"Gryffindor"], 2:[0,"Hufflepuff"], 3:[0,"Ravenclaw"], 4:[0,"Slytherin"]}
    while puntuacion<5 or preguntas<5 or empate:
        puntos_casa = pregunta_el_sombrero()                #la funcion devuelve 1,2,3 o 4 para sumar puntos o veces que se escoge 
        puntuacion = puntuacion + puntos_casa               #este modo suma puntos para evaluar por rango de valores
        casas[puntos_casa][0] = casas[puntos_casa][0] + 1   #este otro modo añade 1 cada vez que se opte por una respuesta de cada casa
        preguntas = preguntas + 1                           #controlo que se hagan min 5 preguntas
        empate = comprueba_empate(casas)                    #evita empates entre casas para facilitar la labor del sombrerito 

    #sistema_puntos_superpop(puntuacion)                     #Con esto activado lanza la selección en funcion de una suma de puntos por pregunta
    sistema_puntos_por_casa(casas.values())                 #con esto activado lanza la selección en función de preferencias de respuesta
""" ------------------------------------------------------------------------------------------------------ """

sombrero_howarts(tu_nombre())           
