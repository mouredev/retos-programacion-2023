<?php

    const LEET = [
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
        'z' => '2'
    ];

    function leetTranslator(string $text):string
    {
        return strtr(strtolower($text), LEET);
    }

    echo leetTranslator('leet')."\n";
    echo leetTranslator('Hello World!')."\n";
    echo leetTranslator('hacker')."\n";
    echo leetTranslator('Aquí está un texto de prueba para ver si funciona el reto!')."\n";

?>