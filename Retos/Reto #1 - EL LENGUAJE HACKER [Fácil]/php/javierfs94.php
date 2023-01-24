<?php
# Reto #1: EL "LENGUAJE HACKER"
#### Dificultad: Fácil | Publicación: 02/01/23 | Corrección: 09/01/23

## Enunciado

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */


const ALPHABET = array(
    'A' => '4',
    'B' => 'I3',
    'C' => '[',
    'D' => ')',
    'E' => '3',
    'F' => '|=',
    'G' => '&',
    'H' => '#',
    'I' => '1',
    'J' => ',_|',
    'K' => '>|',
    'L' => '1',
    'M' => '/\/\\',
    'N' => '^/',
    'O' => '0',
    'P' => '|*',
    'Q' => '(_,)',
    'R' => 'I2',
    'S' => '5',
    'T' => '7',
    'U' => '(_)',
    'V' => '\/',
    'W' => '\/\/',
    'X' => '><',
    'Y' => 'j',
    'Z' => '2',
    '0' => 'o',
    '1' => 'L',
    '2' => 'R',
    '3' => 'E',
    '4' => 'A',
    '5' => 'S',
    '6' => 'b',
    '7' => 'T',
    '8' => 'B',
    '9' => 'g',
);

$text = "Hello World!";

echo getHackerTranslation($text);

function getHackerTranslation($text)
{
    return strtr(strtoupper($text), ALPHABET);
}
