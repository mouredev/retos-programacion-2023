import random


def HogwartsHatSelector():
    print("Bienvenido al Test de Clasificación de Casas de Hogwarts!")
    print("Responde las siguientes preguntas para saber a qué casa pertenecerías:")

    preguntas = ["1. ¿Qué cualidad valoras más en ti mismo?",
                 "2. ¿Qué criatura mágica te gustaría tener como mascota?",
                 "3. ¿Cuál es tu asignatura favorita en Hogwarts?",
                 "4. ¿Cuál es tu lugar favorito en el castillo de Hogwarts?",
                 "5. ¿Cuál es tu hechizo favorito?",
                 "6. ¿Qué objeto mágico te gustaría poseer?",
                 "7. ¿Cuál es tu personaje favorito de Harry Potter?",
                 "8. ¿Qué harías si te enfrentas a un troll?",
                 "9. ¿Qué tipo de clima prefieres?",
                 "10. ¿Cuál es tu forma preferida de transporte mágico?",
                 "11. ¿Qué color te atrae más?",
                 "12. ¿Qué criatura mágica te da más miedo?",
                 "13. ¿Cuál es tu golosina mágica favorita?",
                 "14. ¿Cuál es tu asignatura menos favorita en Hogwarts?",
                 "15. ¿Qué actividad te gustaría hacer en tu tiempo libre en Hogwarts?"]

    opciones = [["a. Coraje", "b. Inteligencia", "c. Lealtad", "d. Astucia"],
                ["a. Búho", "b. Gato", "c. Rata", "d. Lechuza"],
                ["a. Pociones", "b. Transformaciones", "c. Herbología",
                    "d. Defensa contra las Artes Oscuras"],
                ["a. La Sala Común de mi casa", "b. El Gran Comedor",
                    "c. La Biblioteca", "d. Los terrenos del castillo"],
                ["a. Expecto Patronum", "b. Wingardium Leviosa",
                    "c. Expelliarmus", "d. Lumos"],
                ["a. La Capa de Invisibilidad", "b. La Varita de Saúco",
                    "c. El Giratiempo", "d. La Piedra Filosofal"],
                ["a. Harry Potter", "b. Hermione Granger",
                    "c. Ron Weasley", "d. Neville Longbottom"],
                ["a. Huir", "b. Atacar", "c. Pedir ayuda",
                    "d. Intentar razonar con él"],
                ["a. Sol", "b. Lluvia", "c. Nieve", "d. Viento"],
                ["a. Escoba voladora", "b. El Autobús Noctámbulo",
                    "c. El Tren Hogwarts Express", "d. Aparición"],
                ["a. Rojo", "b. Azul", "c. Amarillo", "d. Verde"],
                ["a. Dementor", "b. El Basilisco",
                    "c. El Hombre Lobo", "d. Las Arpías"],
                ["a. Grageas de Todos los Sabores", "b. Chocolate de la Caja de Bertie Bott",
                    "c. Pastel de Calabaza", "d. Caramelos de Menta"],
                ["a. Historia de la Magia", "b. Adivinación",
                    "c. Estudio de los Muggles", "d. Runas Antiguas"],
                ["a. Jugar al Quidditch", "b. Explorar el castillo", "c. Leer en la Biblioteca", "d. Pasar tiempo con amigos"]]

    random_questions = random.sample(range(len(preguntas)), 4)

    respuestas = []
    for i in random_questions:
        print(preguntas[i])
        for opcion in opciones[i]:
            print(opcion)
        respuesta = input("Elige una opción (a, b, c o d): ")
        respuestas.append(respuesta)

    puntuaciones = {"Gryffindor": 0, "Ravenclaw": 0,
                    "Hufflepuff": 0, "Slytherin": 0}

    for respuesta in respuestas:
        if respuesta == "a":
            puntuaciones["Gryffindor"] += 1
        elif respuesta == "b":
            puntuaciones["Ravenclaw"] += 1
        elif respuesta == "c":
            puntuaciones["Hufflepuff"] += 1
        elif respuesta == "d":
            puntuaciones["Slytherin"] += 1

    casa = max(puntuaciones, key=puntuaciones.get)
    return casa


print(
    f"¡Felicidades! Según tus respuestas, perteneces a la casa de {HogwartsHatSelector()}.")
