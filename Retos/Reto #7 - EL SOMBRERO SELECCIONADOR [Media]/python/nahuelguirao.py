def sombrero():
    preguntas = [
        ("¿Que cualidad valoras más de un amigo?", ["1) Coraje","2) Ambición","3) Lealtad", "4) Inteligencia"]),
        ("¿Que actividad prefieres hacer en tu tiempo libre?", ["1) Deporte","2) Planear estrategias","3) Ayudar a otros","4) Leer libros"]),
        ("¿Cual de estas situaciones te da más miedo? ", ["1) Ser humillado en público","2) Fracasar en tus objetivos","3) Perder a un ser querido","4) Estar ignorante"]),
        ("¿Como te describirias? ", ["1) Valiente y decidido","2) Astuto y ambicioso","3) Amable y leal","4) Inteligente y curioso"]),
        ("Si pudieras tener una mascota mágica, ¿cuál elegirías?", ["1) León","2)  Serpiente","3) Tejón","4) Águila"]),
        ]
    
    contadores = {
        "Gryffindor" : 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0,
    }
    
    print("Bienvenido al test de a que casa de Harry Potter perteneces! \n")
    for datos in preguntas:
        print(f"\n{datos[0]}\n")
        for opcion in datos[1]:
            print(f"{opcion}")
        
        respuesta = int(input("Ingrese su respuesta: "))

        if respuesta == 1:
            contadores["Gryffindor"] += 1
        if respuesta == 2:
            contadores["Slytherin"] += 1
        if respuesta == 3:
            contadores["Hufflepuff"] += 1
        if respuesta == 4:
            contadores["Ravenclaw"] += 1
    
    resultado = max(contadores, key=lambda x: contadores[x] )
    print(f"Perteneces a {resultado}!")


sombrero()