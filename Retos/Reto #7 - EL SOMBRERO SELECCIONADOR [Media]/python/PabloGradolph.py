'''
/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
'''
# Obtener el segundo valor de la tupla dada por (puntos, casa)
def obtener_valor(tupla: tuple):
    return tupla[1]

def sombrero_seleccionador() -> str:
    # Definimos las casas que irán sumando puntos según las respuestas dadas.
    puntos = {"Gryffindor": 0, "Slytherin": 0, "Ravenclaw": 0, "Hufflepuff": 0}

    # Definimos las posibles opciones y las preguntas que se harán al usuario.
    opciones = [1,2,3,4]
    preguntas = ['''¿Cómo te gustaría ser recordado?
        1) Como el sabio
        2) Como el bueno
        3) Como el gran
        4) Como el audaz''',
        '''Creas una poción que te garantiza una de las siguientes opciones, escoge la poción:
        1) Sabiduría
        2) Amor
        3) Poder
        4) Gloria''',
        '''¿Cuál preferirías ser?
        1) Querido
        2) De confianza
        3) Envidiado
        4) Alabado''',
        '''Si pudieras tener algún poder, ¿Cuál elegirías?
        1) El poder de leer la mente
        2) El poder de cambiar el pasado
        3) El poder de la fuerza sobrehumana
        4) El poder de la invisibilidad''',
        '''¿Qué camino te tienta más?
        1) La calle adoquinada bordeada de edificios antiguos
        2) El carril amplio, soleado y cubierto de hierba
        3) El camino retorcido y cubierto de hojas a través del bosque
        4) El callegón estrcho, oscuro e iluminado por linternas''']
    
    # Se imprimen todas las preguntas recogiendo la respuesta dada y sumando un punto a la casa correspondiente.
    for i in preguntas:
        print(i)
        opcion = int(input("Inserte la opción deseada: "))
        while opcion not in opciones:
            opcion = int(input("Error, inserte la opción deseada: "))
        if opcion == 1:
            puntos["Ravenclaw"] += 1
        elif opcion == 2:
            puntos["Hufflepuff"] += 1
        elif opcion == 3:
            puntos["Slytherin"] += 1
        else:
            puntos["Gryffindor"] += 1
    
    # Guardamos la casa con mayor valor
    casa = max(puntos.items(), key=obtener_valor)[0]

    # La borramos del diccionario y comprobamos que la puntuación no está repetida
    # La única opción de que esto ocurra es que 2 casas tengan 2 puntos y otra 1.
    del puntos[casa]
    if max(puntos.items(), key=obtener_valor)[1] == 2:
        segunda_casa = max(puntos.items(), key=obtener_valor)[0]
        print(f"Estás entre {casa} y {segunda_casa}")
    else:
        print(f"Pertenece a la casa: {casa}")

if __name__ == "__main__":
    sombrero_seleccionador()
 