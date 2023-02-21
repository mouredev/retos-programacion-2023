<?php

function sortingHat() {
    $questions = array(
        "¿Cuál es tu asignatura favorita?",
        "¿Qué cualidad valoras más en ti?",
        "¿En cuál de estas actividades destacas más?",
        "¿Qué tipo de amigos prefieres?",
        "¿Cuál es tu mayor miedo?"
    );
    $answers = array(
        array("Pociones", "Encantamientos", "Defensa contra las Artes Oscuras", "Adivinación"),
        array("Valentía", "Ambición", "Lealtad", "Inteligencia"),
        array("Deporte", "Música", "Arte", "Lectura"),
        array("Leales y valientes", "Ambiciosos y astutos", "Amistosos y trabajadores", "Intelectuales y curiosos"),
        array("Arañas", "Altura", "Soledad", "Desaprobación de los demás")
    );

    $housePoints = array(
        "Gryffindor" => 0,
        "Slytherin" => 0,
        "Hufflepuff" => 0,
        "Ravenclaw" => 0
    );

    for ($i = 0; $i < count($questions); $i++) {
        echo $questions[$i] . PHP_EOL;

        for ($j = 0; $j < count($answers[$i]); $j++) {
            echo ($j+1) . ") " . $answers[$i][$j] . PHP_EOL;
        }

        $answer = readline("Respuesta: ");

        switch ($answer) {
            case 1:
                $housePoints["Gryffindor"]++;
                break;
            case 2:
                $housePoints["Slytherin"]++;
                break;
            case 3:
                $housePoints["Hufflepuff"]++;
                break;
            case 4:
                $housePoints["Ravenclaw"]++;
                break;
            default:
                echo "Respuesta inválida. Selecciona una opción válida." . PHP_EOL;
                $i--;
                break;
        }
    }

    $maxPoints = max($housePoints);
    $selectedHouse = array_search($maxPoints, $housePoints);

    echo $maxPoints;
    echo "¡Enhorabuena! Has sido seleccionado para la casa " . $selectedHouse . "." . PHP_EOL;
}

sortingHat();

?>
