'''
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
 */
'''

def pregunta1():
    print("Pregunta 1: Ante una sitación peligrosa ¿cómo te definirías? (seleccióna una respuesta):")
    while True:
        respuesta1 = int(input(" 1- valiente\n 2- leal\n 3- aprendes de la situación\n 4- lo piensas antes de actuar\n-> "))
        if respuesta1 in range(1,5):
            break
        else:
            print("Error, selecciona 1,2,3 ó 4")
    return respuesta1

def pregunta2():
    print("Pregunta 2: ¿Cómo eres con tus amigos? (seleccióna una respuesta):")
    while True:
        respuesta2 = int(input(" 1- me gusta compartir tiempo\n 2- soy muy amigable\n 3- prefiero crecer intelectualmente\n 4- suelo ser el líder\n-> "))
        if respuesta2 in range(1,5):
            break
        else:
            print("Error, selecciona 1,2,3 ó 4")
    return respuesta2

def pregunta3():
    print("Pregunta 3: Consigues tus objetivos ¿A través de? (seleccióna una respuesta):")
    while True:
        respuesta3 = int(input(" 1- la determinación\n 2- participar\n 3- aprender de los errores\n 4- la ambición\n-> "))
        if respuesta3 in range(1,5):
            break
        else:
            print("Error, selecciona 1,2,3 ó 4")
    return respuesta3

def pregunta4():
    print("Pregunta 4: ¿Cómo eres en los estudios? (seleccióna una respuesta):")
    while True:
        respuesta4 = int(input(" 1- hago lo que puedo\n 2- soy trabajador\n 3- me gusta estudiar\n 4- no me hace falta estudiar\n-> "))
        if respuesta4 in range(1,5):
            break
        else:
            print("Error, selecciona 1,2,3 ó 4")
    return respuesta4

def pregunta5():
    print("Pregunta 5: Tu color preferido es el (seleccióna una respuesta):")
    while True:
        respuesta5 = int(input(" 1- rojo\n 2- amarillo\n 3- azul\n 4- verde\n-> "))
        if respuesta5 in range(1,5):
            break
        else:
            print("Error, selecciona 1,2,3 ó 4")
    return respuesta5

def calculo(contador, pregunta):
    if pregunta == 1:
        contador[0] += 1
    elif pregunta == 2:
        contador[1] += 1
    elif pregunta == 3:
        contador[2] += 1
    elif pregunta == 4:
        contador[3] += 1
    return contador

def seleccion_casa(contador):
    resultado = ""
    print("---------------------------------------------")
    if contador.index(max(contador)) == 0:
        resultado = "Has sido seleccionado para la casa Gryffindor"
    elif contador.index(max(contador)) == 1:
        resultado = "Has sido seleccionado para la casa Hufflepuff"
    elif contador.index(max(contador)) == 2:
        resultado = "Has sido seleccionado para la casa Ravenclaw"
    elif contador.index(max(contador)) == 3:
        resultado = "Has sido seleccionado para la casa Slytherin"
    return resultado

if __name__ == '__main__':
    print()
    print("El sombrero seleccionador te colocara en la casa que te corresponda, \npor favor, responde a las siguientes preguntas.")
    print()
    input("Presiona 'enter' para continuar")
    print()
    contador = [0,0,0,0]
    print()
    pregunta = pregunta1()
    calculo(contador,pregunta)
    print()
    pregunta = pregunta2()
    calculo(contador,pregunta)
    print()
    pregunta = pregunta3()
    calculo(contador,pregunta)
    print()
    pregunta = pregunta4()
    calculo(contador,pregunta)
    print()
    pregunta = pregunta5()
    calculo(contador,pregunta)
    print()
    print(seleccion_casa(contador))