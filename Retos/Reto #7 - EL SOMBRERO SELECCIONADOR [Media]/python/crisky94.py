# /*
#  * Crea un programa que simule el comportamiento del sombrero seleccionador del
#  * universo mágico de Harry Potter.
#  * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#  * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#  * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#  *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
#  * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#  *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
#  */


def main():
    print("Bienvenido al sombrero seleccionador de Hogwarts")
    print("Responde las siguientes preguntas con la letra de la respuesta que más te identifique")
    print("Pregunta 1: ¿Qué cualidad prefieres?")
    print("a) Valor")
    print("b) Astucia")
    print("c) Lealtad")
    print("d) Inteligencia")
    respuesta1 = input("Respuesta: ")
    print("Pregunta 2: ¿Qué animal prefieres?") 
    print("a) León")    
    print("b) Serpiente")
    print("c) Tejón")
    print("d) Águila")
    respuesta2 = input("Respuesta: ")
    print("Pregunta 3: ¿Qué color prefieres?")  
    print("a) Rojo")    
    print("b) Verde")
    print("c) Amarillo")
    print("d) Azul")
    respuesta3 = input("Respuesta: ")



    casas = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    if respuesta1 == "a":
        casas["Gryffindor"] += 1
    elif respuesta1 == "b":
        casas["Slytherin"] += 1
    elif respuesta1 == "c":
        casas["Hufflepuff"] += 1
    elif respuesta1 == "d":
        casas["Ravenclaw"] += 1
    

    if respuesta2 == "a":
        casas["Gryffindor"] += 1
    elif respuesta2 == "b":
        casas["Slytherin"] += 1
    elif respuesta2 == "c":
        casas["Hufflepuff"] += 1
    elif respuesta2 == "d":
        casas["Ravenclaw"] += 1

    if respuesta3 == "a":
        casas["Gryffindor"] += 1
    elif respuesta3 == "b":
        casas["Slytherin"] += 1
    elif respuesta3 == "c":
        casas["Hufflepuff"] += 1
    elif respuesta3 == "d":
        casas["Ravenclaw"] += 1


    casa = max(casas, key=casas.get)
    print(f"Tu casa es: {casa}")

if __name__ == "__main__":
    main()
