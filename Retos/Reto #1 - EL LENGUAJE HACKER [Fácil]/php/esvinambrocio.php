<?php

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 *
 * Version: PHP 8.2
 */

declare(strict_types=1);

const ALPHABET = [
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
    'a' => '4',
    'b' => 'I3',
    'c' => '[',
    'd' => ')',
    'e' => '3',
    'f' => '|=',
    'g' => '&',
    'h' => '#',
    'i' => '1',
    'j' => ',_|',
    'k' => '>|',
    'l' => '1',
    'm' => '/\\/\\',
    'n' => '^/',
    'o' => '0',
    'p' => '|*',
    'q' => '(_,)',
    'r' => 'I2',
    's' => '5',
    't' => '7',
    'u' => '(_)',
    'v' => '\\/',
    'w' => '\\/\\/',
    'x' => '><',
    'y' => 'j',
    'z' => '2',
];

function removeAccents(string $input): string
{
    $textHtmlEntities = htmlentities($input, ENT_QUOTES, 'UTF-8');
    $removeAccents = preg_replace('~&([a-z]{1,2})(acute|cedil|circ|grave|lig|orn|ring|slash|th|tilde|uml);~i', '$1', $textHtmlEntities);
    $text = html_entity_decode($removeAccents);
    return $text;
}

function strToLeet(string $input): string
{
    return strtr(strtolower($input), ALPHABET);
}
$text =  readline("Ingresa texto: ");

echo strToLeet(removeAccents($text));
echo "\n";
