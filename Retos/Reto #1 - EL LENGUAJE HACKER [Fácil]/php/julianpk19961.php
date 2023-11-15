<?php

/**
 * Reto #1: EL "LENGUAJE HACKER"
 *  Enunciado
 *  Escribe un programa que reciba un texto y transforme lenguaje natural a
 *  "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 *  Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *  con el alfabeto y los números en "leet".
 *  (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */


$transform = [
    "a" => "4",
    "b" => "I3",
    "c" => "[",
    "d" => ")",
    "e" => "3",
    "f" => "|=",
    "g" => "&",
    "h" => "#",
    "i" => "1",
    "j" => ",_|",
    "k" => ">|",
    "l" => "1",
    "m" => "/\/\'",
    "n" => "^/",
    "ñ" => "~",
    "o" => "0",
    "p" => "|*",
    "q" => "(_,)",
    "r" => "|2",
    "s" => "5",
    "t" => "7",
    "u" => "(_)",
    "v" => "\/",
    "w" => "\/\/",
    "x" => "><",
    "y" => "j",
    "z" => "2",
    "0" => "o",
    "1" => "L",
    "2" => "R",
    "3" => "E",
    "4" => "A",
    "5" => "S",
    "6" => "b",
    "7" => "T",
    "8" => "B",
    "9" => "g",
];

$exceptionsChar = [" ", ".", ",", "'"];

function sentencesToLeet($sentence = 'Sentence is void')
{

    global $transform, $exceptionsChar;

    if (gettype($sentence)  === 'object') {
        $sentence = "I Can't work with a object, sorry";
    }

    if (gettype($sentence)  === 'array') {
        $sentence = implode($sentence);
    }

    $leetSentences = str_split(strtolower($sentence));

    foreach ($leetSentences as $character) {
        $key = str_replace($exceptionsChar, "", $character);
        if ($key) {
            echo $transform[$key];
        } else {
            echo $character;
        }
    };
    echo "\n";
}


sentencesToLeet(new stdClass);
sentencesToLeet(["this", "an", "array"]);
sentencesToLeet(25660);
sentencesToLeet(25, 5);
sentencesToLeet(25.5);
sentencesToLeet("Hello");