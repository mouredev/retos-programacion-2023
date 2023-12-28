<?php

declare(strict_types=1);

/**
 * The function "leet" takes a string as input and returns a leet (1337) version of the string by
 * replacing certain characters with their leet equivalents.
 * 
 * @param int|string The parameter "text" is a string or an integer that represents the text to be
 * converted into leet (1337) language.
 * 
 * @return string a string that has been converted to "leet" or "1337" speak.
 */
function leet(int|string $text): string
{
    $leetText = '';
    $vocabulary = [
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
        'm' => '/\/\\',
        'n' => '^/',
        'o' => '0',
        'p' => '|*',
        'q' => '(_,)',
        'r' => 'I2',
        's' => '5',
        't' => '7',
        'u' => '(_)',
        'v' => '\/',
        'w' => '\/\/',
        'x' => '><',
        'y' => 'j',
        'z' => '2',
        '1' => 'L',
        '2' => 'R',
        '3' => 'E',
        '4' => 'A',
        '5' => 'S',
        '6' => 'b',
        '7' => 'T',
        '8' => 'B',
        '9' => 'g',
        '0' => 'o',
    ];

    foreach (str_split(strval($text)) as $letter) {
        $leetText .= $vocabulary[$letter];
    }
    return $leetText;
}

/* The code `echo leet(123); echo leet("kodingrick");` is calling the `leet()` function twice with
different arguments and then printing the returned leet versions of the input strings. */
echo leet(123) . PHP_EOL;
echo leet("kodingrick") . PHP_EOL;
