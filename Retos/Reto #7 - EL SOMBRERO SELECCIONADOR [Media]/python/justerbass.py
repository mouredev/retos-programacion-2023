import random

expresiones = ["hummmm", "Interesante", "aja!!!", "pues claro", "....", "si tu lo dices"]

preguntas = ["Entras en un jardín encantado. ¿Qué sería lo más curioso de examinar primero?",
            "Las setas rojas gordas que parecen estar hablando entre sí",
            "El estanque burbujeante en cuyas profundidades se arremolina algo luminoso",
            "El árbol de hojas de plata con manzanas doradas", 
            "La estatua del viejo mago con un extraño centelleo en los ojos", 
            "Se colocan cuatro cajas ante ti, ¿cuál intentarías abrir?",
            "La pequeña caja de peltre, sencilla y sencilla, con un mensaje rayado que dice: Abro sólo para los dignos",
            "El ataúd dorado adornado, de pie sobre patas con garras, cuya inscripción advierte que tanto el conocimiento secreto como la tentación insoportable se encuentran dentro.",
            "La reluciente caja de color negro azabache con una cerradura y una llave plateadas, marcada con una runa misteriosa que sabes que es la marca de Merlín",
            "La caja pequeña de carey adornada con oro, en cuyo interior parece chillar una pequeña criatura",
            "Se colocan cuatro copas ante ti. ¿Qué elegirías para beber?",
            "El líquido dorado tan brillante que duele la vista y que hace bailar las manchas solares por toda la habitación.",
            "La bebida suave, espesa y de un color púrpura intenso que desprende un delicioso olor a chocolate y ciruelas.",
            "El líquido espumoso, espumoso y plateado que brilla como si tuviera diamantes molidos.",
            "El misterioso líquido negro que reluce como tinta y desprende humos que te hacen ver extrañas visiones",
            "Si pudieras tener algún poder, ¿cuál elegirías?",
            "El poder de leer la mente",
            "El poder de la invisibilidad",
            "El poder de cambiar tu apariencia a voluntad",
            "El poder de la fuerza sobrehumana",
            "¿Que camino te tienta más?",
            "El callejón estrecho, oscuro e iluminado por linternas",
            "La calle adoquinada bordeada de edificios antiguos",
            "El carril amplio, soleado y cubierto de hierba",
            "El camino retorcido y cubierto de hojas a través del bosque"]

def consultas():

    Slytherin = 0
    Ravenclaw = 0
    Hufflepuff = 0
    Gryffindor = 0

    for i in range(0,len(preguntas),5):
        print()
        print(preguntas[i])
        print()
        print(f"A) {preguntas[i+1]}")
        print(f"B) {preguntas[i+2]}")
        print(f"C) {preguntas[i+3]}")
        print(f"D) {preguntas[i+4]}")
        print()
        while True:
            respuesta =  input("ingrese respuesta => ").lower()
            
            alternativas = ["a", "b", "c", "d"]
            if not respuesta in alternativas:
                print("respuesta no valida")
            else:
                print ("el sombrero dice: " + random.choice(expresiones))
                break
        
        alternativa = respuesta

        if alternativa == "a":
            Slytherin += 1
        elif alternativa == "b":
            Ravenclaw += 1  
        elif alternativa == "c":
            Hufflepuff += 1
        elif alternativa == "d":
            Gryffindor += 1

    return Slytherin, Ravenclaw, Hufflepuff, Gryffindor

def eleccion():

    azar = ["Slytherin", "Ravenclaw", "Hufflepuff", "Gryffindor"]

    total = consultas()
    if total[0] > total[1] and total[0] > total[2] and total[0] > total[3]:
        print("tu casa es SLYTHERIN!!!")
    elif total[1] > total[0] and total[1] > total[2] and total[1] > total[3]:
        print("tu casa es RAVENCLAW!!!")
    elif total[2] > total[1] and total[2] > total[0] and total[2] > total[3]:
        print("tu casa es HUFFLEPUFF!!!")
    elif total[3] > total[1] and total[3] > total[2] and total[3] > total[0]:
        print("tu casa es GRYFFINDOR!!!")
    else:
        for house in range(4):
            no_se = random.choice(azar)
        print(f"tu casa es {no_se} !!!")

def sombrero():
    eleccion()
    return print("Que disfrutes del banquete y tu nueva casa.")

sombrero()
