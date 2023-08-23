<?php

declare(strict_types=1);

echo "\033[2J\033[H";

$questions = [
    '¿Qué tipo de lugar te parece más fascinante?' =>
    [
        '1.- Un bosque misterioso.' => 'Hufflepuff',
        '2.- Una montaña imponente.' => 'Gryffindor',
        '3,- Un océano infinito.' => 'Ravenclaw',
        '4.- Un desierto enigmático.' => 'Slytherin'
    ],
    'Ante un desafío, ¿cuál es tu enfoque principal?' =>
    [
        '1.- Utilizar la astucia y la inteligencia.' => 'Ravenclaw',
        '2.- Actuar con valentía y determinación.' => 'Gryffindor',
        '3,- Mantener la calma y la paciencia.' => 'Hufflepuff',
        '4.- Confiar en mi intuición y creatividad.' => 'Slytherin'
    ],
    'En una aventura, ¿qué objeto elegirías llevar contigo?' =>
    [
        '1.- Un libro lleno de conocimiento.' => 'Ravenclaw',
        '2.- Una espada reluciente.' => 'Gryffindor',
        '3,- Un amuleto especial de un ser querido.' => 'Hufflepuff',
        '4.- Un mapa que muestra ubicaciones ocultas.' => 'Slytherin'
    ],
    '¿Cuál de los siguientes valores es más importante para ti?' =>
    [
        '1.- Sabiduría y aprendizaje.' => 'Ravenclaw',
        '2.- Coraje y valentía.' => 'Gryffindor',
        '3,- Lealtad y amistad.' => 'Hufflepuff',
        '4.- Originalidad y curiosidad.' => 'Slytherin'
    ],
    'En tu tiempo libre, ¿qué actividad te atrae más?' =>
    [
        '1.- Resolver acertijos y rompecabezas.' => 'Ravenclaw',
        '2.- Practicar deportes y actividades físicas.' => 'Gryffindor',
        '3,- Pasar tiempo con amigos y seres queridos.' => 'Hufflepuff',
        '4.- Explorar lugares desconocidos y asombrosos.' => 'Slytherin'
    ],
];

$score = [
    'Gryffindor' => 0,
    'Hufflepuff' => 0,
    'Ravenclaw' => 0,
    'Slytherin' => 0
];


/**
 * The function "choose" takes an option and an array of answers, and increments the score for the
 * selected answer.
 * 
 * @param int option The option parameter is an integer that represents the selected option.
 * @param array answers The `` parameter is an array that contains a list of possible answers.
 * Each answer is represented by a string value.
 */
function choose(int $option, array $answers): void
{
    global $score;
    $score[$answers[$option - 1]]++;
}

/* The code block you provided is responsible for asking the user a series of questions and collecting
their answers. */
foreach ($questions as $question => $answers) {
    do {
        echo $question . PHP_EOL;
        foreach ($answers as $answer => $value) {
            echo $answer . PHP_EOL;
        }
        $answer = readline('Escoge: ');
    } while ($answer < 1 || $answer > 4);
    choose((int)$answer, array_values($answers));
    echo "\033[2J\033[H";
}


$values = array_keys($score, max($score), true);

if (count($values) > 1) {
    echo 'Ha estado algo complicado, seras ' . $values[rand(0, count($values) - 1)];
} else {
    echo 'Esta claro, seras ' . $values[0];
}
