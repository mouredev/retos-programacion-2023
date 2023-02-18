const HogwartsHatSelector = () => {
    console.log("Bienvenido al Test de Clasificación de Casas de Hogwarts!");
    console.log("Responde las siguientes preguntas para saber a qué casa pertenecerías:");

    const preguntas = ["1. ¿Qué cualidad valoras más en ti mismo?",
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
                    "15. ¿Qué actividad te gustaría hacer en tu tiempo libre en Hogwarts?"];

    const opciones = [["a. Coraje", "b. Inteligencia", "c. Lealtad", "d. Astucia"],
                    ["a. Búho", "b. Gato", "c. Rata", "d. Lechuza"],
                    ["a. Pociones", "b. Transformaciones", "c. Herbología", "d. Defensa contra las Artes Oscuras"],
                    ["a. La Sala Común de mi casa", "b. El Gran Comedor", "c. La Biblioteca", "d. Los terrenos del castillo"],
                    ["a. Expecto Patronum", "b. Wingardium Leviosa", "c. Expelliarmus", "d. Lumos"],
                    ["a. La Capa de Invisibilidad", "b. La Varita de Saúco", "c. El Giratiempo", "d. La Piedra Filosofal"],
                    ["a. Harry Potter", "b. Hermione Granger", "c. Ron Weasley", "d. Neville Longbottom"],
                    ["a. Huir", "b. Atacar", "c. Pedir ayuda", "d. Intentar razonar con él"],
                    ["a. Sol", "b. Lluvia", "c. Nieve", "d. Viento"],
                    ["a. Escoba voladora", "b. El Autobús Noctámbulo",
                    "c. El Tren Hogwarts Express", "d. Aparición"],
                    ["a. Rojo", "b. Azul", "c. Amarillo", "d. Verde"],
                    ["a. Dementor", "b. El Basilisco", "c. El Hombre Lobo", "d. Las Arpías"],
                    ["a. Grageas de Todos los Sabores", "b. Chocolate de la Caja de Bertie Bott",
                    "c. Pastel de Calabaza", "d. Caramelos de Menta"],
                    ["a. Historia de la Magia", "b. Adivinación",
                    "c. Estudio de los Muggles", "d. Runas Antiguas"],
                    ["a. Jugar al Quidditch", "b. Explorar el castillo", "c. Leer en la Biblioteca", "d. Pasar tiempo con amigos"]];

    // Elegimos cuatro preguntas al azar
    const random_questions = [];
    while (random_questions.length < 4) {
    const random = Math.floor(Math.random() * preguntas.length);
    if (!random_questions.includes(random)) {
        random_questions.push(random);
    }
    }

    const respuestas = [];
    for (const i of random_questions) {
    console.log(preguntas[i]);
    for (const opcion of opciones[i]) {
        console.log(opcion);
    }
    const respuesta = prompt("Elige una opción (a, b, c o d): ");
    respuestas.push(respuesta);
    }

    const puntuaciones = {"Gryffindor": 0, "Ravenclaw": 0, "Hufflepuff": 0, "Slytherin": 0};

    for (const respuesta of respuestas) {
    if (respuesta === "a") {
        puntuaciones["Gryffindor"] += 1;
    } else if (respuesta === "b") {
        puntuaciones["Ravenclaw"] += 1;
    } else if (respuesta === "c") {
        puntuaciones["Hufflepuff"] += 1;
    } else if (respuesta === "d") {
        puntuaciones["Slytherin"] += 1;
    }
    }

    const casa = Object.keys(puntuaciones).reduce((a, b) => puntuaciones[a] > puntuaciones[b] ? a : b);
    return '¡Felicidades! Según tus respuestas, perteneces a la casa de ' + casa
}

console.log(HogwartsHatSelector());