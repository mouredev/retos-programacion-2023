<?php

declare(strict_types=1);

/**
 * The function "leet" takes a string or integer as input and converts it to leet (1337) speak by
 * replacing certain characters with their leet equivalents.
 * 
 * @param string txt The `txt` parameter in the `leet` function is the input text that you want to
 * convert to leet (1337) language. It can be either a string or an integer.
 * 
 * @return string The function `leet` returns a string that is the leet (or "1337") version of the
 * input text.
 */
function leet(string|int $txt): string
{
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
        '1' => 'l',
        '2' => 'r',
        '3' => 'e',
        '4' => 'a',
        '5' => 's',
        '6' => 'b',
        '7' => 't',
        '8' => 'b',
        '9' => 'g',
        '0' => 'o'
    ];
    $result = '';
    foreach (str_split((string)$txt) as $letter) {
        $result .= $vocabulary[$letter];
    }

    return $result . PHP_EOL;
}

/* The line `echo leet('hola leet');` is calling the `leet` function and passing the string `'hola
leet'` as an argument. The function will convert the input text to leet (1337) speak and return the
result. The `echo` statement then outputs the result to the console. */
echo leet('hola leet');
