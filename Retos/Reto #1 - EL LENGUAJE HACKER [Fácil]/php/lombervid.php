<?php
declare(strict_types=1);

function strToLeet(string $input): string
{
    $alphabet = [
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

    return strtr(strtolower($input), $alphabet);
}

// Main code
$cases = [
    'demo' => ')3/\/\0',
    'hacker' => '#4[>|3I2',
    'H4x0r' => '#A><oI2',
    'Hello World!' => '#3110 \/\/0I21)!',
    'My password is: 17o^DuQn$qNj' => "/\/\j |*455\/\/0I2) 15: LT0^)(_)(_,)^/$(_,)^/,_|",
];

foreach ($cases as $input => $want) {
    $got = strToLeet($input);

    if ($want === $got) {
        print("Case passed:");
    } else {
        print("Case failed");
    }

    printf("\n\tinput:\t\"%s\"\n\twant:\t\"%s\"\n\tgot:\t\"%s\"\n\n", $input, $want, $got);
}
