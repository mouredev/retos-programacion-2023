<?php

function generatePassword($length = 8, $hasCapitalLetters = true, $hasNumbers = true, $hasSymbols = true): string
{
    if($length < 8 || $length > 16) return "Invalid length";

    $validCharacters = range('a', 'z');

    $otherCharacters = [
        'CapitalLetters' => range('A', 'Z'),
        'Numbers' => range(0, 9),
        'Symbols' => array_filter(range('!', '/'), function ($letter) {
            return !in_array($letter, ['"', '\'']);
        })
    ];

    $password = [];

    $password[] .=  $validCharacters[array_rand($validCharacters)];

    foreach ($otherCharacters as $type => $characters) {
        $hasCharacters = 'has' . $type;

        if($$hasCharacters) {
            $password[] .=  $characters[array_rand($characters)];
            $validCharacters = array_merge($validCharacters, $characters);
        }
    }

    $length -= count($password);

    for ($i = 0; $i < $length ; $i++) {
        $password[] .=  $validCharacters[array_rand($validCharacters)];
    }

    shuffle($password);

    return implode("", $password);
}

echo "Password: " . generatePassword(8, false, false, false) . "\n";
echo "Password: " . generatePassword(9, true, false, false) . "\n";
echo "Password: " . generatePassword(10, false, true, false) . "\n";
echo "Password: " . generatePassword(11, false, false, true) . "\n";
echo "Password: " . generatePassword(12) . "\n";
