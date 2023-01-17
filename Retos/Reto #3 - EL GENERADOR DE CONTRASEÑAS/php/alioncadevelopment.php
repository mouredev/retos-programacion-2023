<?php

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

function generatePassword($length, $uppercase, $numbers, $symbols) {
    if ($length <= 8 || $length => 16) {
        echo "Error: password length must be between 8 and 16";
        return;
    }
    $uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    $numbers_chars = "0123456789";
    $symbols_chars = "!@#%^&*()-_=+";
    $all_chars = "abcdefghijklmnopqrstuvwxyz" . $uppercase_chars . $numbers_chars . $symbols_chars;
    $password = "";
    for ($i = 0; $i < $length; $i++) {
        if ($uppercase) {
            $password .= $uppercase_chars[rand(0, strlen($uppercase_chars) - 1)];
        }
        if ($numbers) {
            $password .= $numbers_chars[rand(0, strlen($numbers_chars) - 1)];
        }
        if ($symbols) {
            $password .= $symbols_chars[rand(0, strlen($symbols_chars) - 1)];
        }
        $password .= $all_chars[rand(0, strlen($all_chars) - 1)];
    }
    return $password;
}

// Example usage:
$length = 12;
$uppercase = true;
$numbers = true;
$symbols = true;
$password = generatePassword($length, $uppercase, $numbers, $symbols);
echo "Your generated password is: " . $password;

?>
