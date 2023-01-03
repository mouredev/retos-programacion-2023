<?php
/** 
 * Challenge #1 - The Hacker Language
 * 
 * @author kevocde <kevocde@gmail.com>
 */

const REPLACERS = [
    'A' => "4",
    'B' => "I3",
    'C' => "[",
    'D' => ")",
    'E' => "3",
    'F' => "|=",
    'G' => "&",
    'H' => "#",
    'I' => "1",
    'J' => ",_|",
    'K' => ">|",
    'L' => "1",
    'M' => "/\/\\",
    'N' => "^/",
    'O' => "0",
    'P' => "|*",
    'Q' => "(_,)",
    'R' => "I2",
    'S' => "5",
    'T' => "7",
    'U' => "(_)",
    'V' => "\/",
    'W' => "\/\/",
    'X' => "><",
    'Y' => "j",
    'Z' => "2",
    '1' => 'L',
    '2' => 'R',
    '3' => 'E',
    '4' => 'A',
    '5' => 'S',
    '6' => 'b',
    '7' => '8',
    '8' => 'B',
    '9' => 'g',
    '0' => 'o',
];

/**
 * Translate some text to leet language
 *
 * @param [type] $text
 * @param integer $depth
 * @return string
 */
function translateToLeet($text): string {
    $text = array_map(
        function ($character) {
            return REPLACERS[$character] ?? $character; // for each caracter finds their equivalence an return
        },
        str_split(strtoupper($text)) // converts the input to uppercase later to array with each character
    );
    return implode($text); // To end, converts to string again
}

$input = readline('Write the word to translate: ');
echo translateToLeet($input) . "\n";
