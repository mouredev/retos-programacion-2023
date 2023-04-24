<?php

function generatePassword($length, $withUppercase, $withNumbers, $withSymbols) {

    $minus = range('a', 'z');
    $uppers = range('A', 'Z');
    $numbers = range(0, 9);
    $symbols = ['!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=','>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'];

    $characters = [];
    $password = '';

    if (!is_int($length) || $length < 8 || $length > 16) {
        throw new Exception("La longitud debe ser un número entero entre 8 y 16.");
    }
    if (!is_bool($withUppercase) || !is_bool($withNumbers) || !is_bool($withSymbols)) {
        throw new Exception("Los parámetros uppercase, numbers, symbols deben ser booleanos.");
    }

    $withUppercase && $characters = array_merge($characters, $uppers);

    $withNumbers && $characters = array_merge($characters, $numbers);

    $withSymbols && $characters = array_merge($characters, $symbols);

    $characters = array_merge($characters, $minus);

    for ($i = 0; $i < $length; $i++) {
        $password .= $characters[array_rand($characters)];
    }

    return $password;
}

echo generatePassword(16, true, true, true) . "\n";
echo generatePassword(12, false, true, false) . "\n";
echo generatePassword(8, true, false, true) . "\n";