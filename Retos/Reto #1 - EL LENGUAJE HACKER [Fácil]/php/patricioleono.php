<?php
$lenguageHacker = array(
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
    'ñ' => '^/',
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
    '0' => 'o',
    '1' => 'L',
    '2' => 'R',
    '3' => 'E',
    '4' => 'A',
    '5' => 'S',
    '6' => 'b',
    '7' => 'T',
    '8' => 'B',
    '9' => 'g'
);


$word = 'Patricio Leon Termino este RETO';

function reemplaceAndPrint($word, $lang){
    print "Palabra Hacker: " .strtr(strtolower($word), $lang);
    print "\n";
}

print "Palabra Normal: ". $word;
print "\n";
reemplaceAndPrint($word, $lenguageHacker);