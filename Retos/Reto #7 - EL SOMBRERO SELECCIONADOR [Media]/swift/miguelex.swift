import Foundation

func hogwartsHatSelector() {
    print("Bienvenido al Test de Clasificación de Casas de Hogwarts!")
    print("Responde las siguientes preguntas para saber a qué casa pertenecerías:")
    let preguntas = [
        "1. ¿Qué cualidad valoras más en ti mismo?",
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
        "15. ¿Qué actividad te gustaría hacer en tu tiempo libre en Hogwarts?"
    ]
    let opciones = [
        ["a. Coraje", "b. Inteligencia", "c. Lealtad", "d. Astucia"],
        ["a. Búho", "b. Gato", "c. Rata", "d. Lechuza"],
        ["a. Pociones", "b. Transformaciones", "c. Herbología", "d. Defensa contra las Artes Oscuras"],
        ["a. La Sala Común de mi casa", "b. El Gran Comedor", "c. La Biblioteca", "d. Los terrenos del castillo"],
        ["a. Expecto Patronum", "b. Wingardium Leviosa", "c. Expelliarmus", "d. Lumos"],
        ["a. La Capa de Invisibilidad", "b. La Varita dNeville Longbottom", "d. Draco Malfoy"],
        ["a. Huir", "b. Atacar", "c. Pedir ayuda", "d. Intentar razonar con él"],
        ["a. Sol", "b. Lluvia", "c. Nieve", "d. Viento"],
        ["a. Escoba voladora", "b. El Autobús Noctámbulo", "c. El Tren Hogwarts Express", "d. Aparición"],
        ["a. Rojo", "b. Azul", "c. Amarillo", "d. Verde"],
        ["a. Dementor", "b. El Basilisco", "c. El Hombre Lobo", "d. Las Arpías"],
        ["a. Grageas de Todos los Sabores", "b. Chocolate de la Caja de Bertie Bott", "c. Pastel de Calabaza", "d. Caramelos de Menta"],
        ["a. Historia de la Magia", "b. Adivinación", "c. Estudio de los Muggles", "d. Runas Antiguas"],
        ["a. Jugar al Quidditch", "b. Explorar el castillo", "c. Leer en la Biblioteca", "d. Pasar tiempo con amigos"]
    ]

    
    // Elegimos cuatro preguntas al azar
    var randomQuestions = Set<Int>()
    while randomQuestions.count < 4 {
        let random = Int.random(in: 0..<preguntas.count)
        randomQuestions.insert(random)
    }

    var respuestas = [String]()
    for i in randomQuestions {
        print(preguntas[i])
        for opcion in opciones[i] {
            print(opcion)
        }
        print("Elige una opción (a, b, c o d): ")
        if let respuesta = readLine() {
            respuestas.append(respuesta)
        }
    }

    var puntuaciones = [
        "Gryffindor": 0,
        "Ravenclaw": 0,
        "Hufflepuff": 0,
        "Slytherin": 0
    ]
    for respuesta in respuestas {
        switch respuesta {
            case "a":
                puntuaciones["Gryffindor"]! += 1
            case "b":
                puntuaciones["Ravenclaw"]! += 1
            case "c":
                puntuaciones["Hufflepuff"]! += 1
            case "d":
                puntuaciones["Slytherin"]! += 1
            default:
                break
        }
    }

    let casa = puntuaciones.max(by: { $0.value < $1.value })?.key ?? ""
    print("Enhorabuena!! tu casa es: " + casa)
}

hogwartsHatSelector()