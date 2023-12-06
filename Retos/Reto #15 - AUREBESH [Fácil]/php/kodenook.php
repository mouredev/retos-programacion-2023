<?php

declare (strict_types = 1);

/**
 * The `aurebesh` function translates a given string into a fictional language called Aurebesh, using a
 * predefined mapping of letters.
 *
 * @param string txt The `txt` parameter is a string that represents the text that needs to be
 * translated into Aurebesh.
 *
 * @return string a string that has been translated from English to Aurebesh.
 */
function aurebesh(string $txt): string
{
    $translated = [];
    $letters = [
        'a' => 'aur',
        'b' => 'besh',
        'c' => 'cresh',
        'd' => 'dorn',
        'e' => 'esh',
        'f' => 'forn',
        'g' => 'gol',
        'h' => 'herf',
        'i' => 'is',
        'j' => 'jenth',
        'k' => 'kran',
        'l' => 'lor',
        'm' => 'mar',
        'n' => 'nal',
        'o' => 'oth',
        'p' => 'pal',
        'q' => 'quen',
        'r' => 'res',
        's' => 'sin',
        't' => 'tor',
        'u' => 'ul',
        'v' => 'ver',
        'w' => 'wor',
        'x' => 'xesh',
        'y' => 'yen',
        'z' => 'zorn',
    ];

    $txt = str_split(mb_strtolower($txt));

    foreach ($txt as $value) {
        array_push($trans, $letters[$value] ?? $value);
    }

    return implode('', $trans);
}

echo aurebesh('hello there');
