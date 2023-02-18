<?php

function HogwartsHatSelector() {
    $preguntas = [
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
    ];

    $opciones = [
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
    ];

    echo "Bienvenido al Test de Clasificación de Casas de Hogwarts!\n";
    echo "Responde las siguientes preguntas para saber a qué casa pertenecerías:\n";

    // Elegimos cuatro preguntas al azar
    $random_questions = array_rand($preguntas, 4);

    $respuestas = [];
    foreach ($random_questions as $i) {
        echo $preguntas[$i] . "\n";
        foreach ($opciones[$i] as $opcion) {
            echo $opcion . "\n";
        }
        $respuesta = readline("Elige una opción (a, b, c o d): ");
        $respuestas[] = $respuesta;
    }

    $puntuaciones = ["Gryffindor" => 0, "Ravenclaw" => 0, "Hufflepuff" => 0, "Slytherin" => 0];

    foreach ($respuestas as $respuesta) {
        if ($respuesta == "a") {
            $puntuaciones["Gryffindor"]++;
        } elseif ($respuesta == "b") {
            $puntuaciones["Ravenclaw"]++;
        } elseif ($respuesta == "c") {
            $puntuaciones["Hufflepuff"]++;
        } elseif ($respuesta == "d") {
            $puntuaciones["Slytherin"]++;
        }
    }

    $casa = array_search(max($puntuaciones), $puntuaciones);
    return $casa;
}

echo "¡Felicidades! Según tus respuestas, perteneces a la casa de ".HogwartsHatSelector();
?>