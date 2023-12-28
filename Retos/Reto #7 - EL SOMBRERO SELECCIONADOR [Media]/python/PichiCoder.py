# 5 preguntas (como mínimo) a través de la terminal. 
# Cada pregunta tendrá 4 respuestas posibles (a seleccionar por terminal).
# Mayor cantidad de A = Slytherin; de B = Hufflepuff; de C = Ravenclaw; de D = Gryffindor

# Gryffindor: valentía, disposición, coraje y caballerosidad
# Hufflepuff: leales, honestos y que no teman el trabajo pesado.
# Ravenclaw: creativos, curiosos y que siempre busquen la respuesta.
# Slytherin: ambición y la astucia.

def check_Answer(): 
    respuesta = ""
    while respuesta not in ["a","b","c","d"]:
        respuesta = input("Ingresar respuesta: ").lower()
    return respuesta

def sombrero_Seleccionador():
    respuestas = {}
    
    # Primer Pregunta
    print("Si tuvieses que traicionar a tu familia y amigos para ser el mejor mago de la historia, ¿Lo harias?")
    print("Opcion (A): Si y no sentiria ningun remordimiento, estaria orgulloso.\nOpcion (B): Reflexionaria demasiado pero seguramente lo terminaria haciendo.\nOpcion (C): Lo haria solo si fuese la unica manera de protejerlos.\nOpcion (D): Jamas, buscaria cualquier otra alternativa para serlo.")
    ans = check_Answer()
    respuestas[ans] = respuestas.get(ans,0) + 1
    
    # Segunda Pregunta
    print("¿Serias capaz de elaborar un libro de hechizos basicos que ayude a los alumnos novatos?")
    print("Opcion (A): No valdria la pena, para eso estan los profesores.\nOpcion (B): Si, aunque no lo haria gratis.\nOpcion (C): Si, me seria muy util para practicar.\nOpcion (D): Por supuesto, ademas podria dar tutorias a los de primer año.")
    ans = check_Answer()
    respuestas[ans] = respuestas.get(ans,0) + 1
    
    # Tercera Pregunta
    print("¿Darias tu vida por salvar a tus amigos?")
    print("Opcion (A): Espero nunca encontrarme en esa situacion, no lo se.\nOpcion (B): Si por amigos te refieres a los incondicionales... pues creo que si.\nOpcion (C): Creo que podria encontrar otra forma de salvarlos sin morir, o no?.\nOpcion (D): Sin dudarlo ni un segundo.")
    ans = check_Answer()
    respuestas[ans] = respuestas.get(ans,0) + 1
    
    # Cuarta Pregunta
    print("¿Alguna vez hablaste con las serpientes?")
    print("Opcion (A): Si, varias veces y fue divertido.\nOpcion (B): No sabria como hacerlo.\nOpcion (C): No, pero seria curioso poder hacerlo.\nOpcion (D): ¿Por que lo haria? No lo necesito.")
    ans = check_Answer()
    respuestas[ans] = respuestas.get(ans,0) + 1
    
    # Quinta Pregunta
    print("¿Que opinas de ese tal Potter y sus amigos?")
    print("Opcion (A): Baah, esos muchachos no me caen nada bien.\nOpcion (B): No los conozco.\nOpcion (C): Me parecen divertidos, me caen bien.\nOpcion (D): Son lo máximo, quisiera ser como ellos algun dia!")
    ans = check_Answer()
    respuestas[ans] = respuestas.get(ans,0) + 1
    
    #Seleccion   
    max = 0
    eleccion = ""
    for an, count in respuestas.items():
        if count >= max:
            eleccion = an

    casas = {"a":"Slytherin", "b":"Hufflepuff", "c":"Ravenclaw", "d":"Gryffindor"}
    
    return print("Has sido seleccionado para entrar a la casa "+casas[eleccion])
   
sombrero_Seleccionador()
