
<?php
# Reto #3: EL GENERADOR DE CONTRASEÑAS
#### Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23

## Enunciado


/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

header('Content-Type: text/html; charset=UTF-8');
function generatePassword($length, array $options)
{
    $characters = [
        "lower_letters" => "abcdefghijklmnñopqrstuvwxyz",
        "upper_letters" => "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "numbers" => "1234567890",
        "symbols" => "{!@#$%^&*()-_+=<>?/.,}"
    ];

    $allowedCharacters = "";
    foreach ($options as $key => $option) {
        if ($option) {
            $allowedCharacters .= $characters[$key];
        }
    }

    $password = "";
    for ($i = 0; $i < $length; $i++) {
        $password .= $allowedCharacters[rand(0, strlen($allowedCharacters) - 1)];
    }

    return $password;
}

$length = 14;
$options = [
    "lower_letters" => false,
    "upper_letters" => true,
    "numbers" => true,
    "symbols" => false
];

echo "Your new password: " . generatePassword($length, $options);

?>