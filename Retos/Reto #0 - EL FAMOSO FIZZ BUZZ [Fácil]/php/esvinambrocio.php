<?php

/**
 * Reto #0: EL FAMOSO "FIZZ BUZZ"
 * Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23
 *
 * Version: PHP 8.2
 *
 * Enunciado
 *
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

const QUANTITY_PRINTS = 100;

$i = 1;
while ($i <= QUANTITY_PRINTS) {
    $wordToPrint = "";
    $isMultiploThree = is_multiplo($i, 3);
    $isMultiploFive = is_multiplo($i, 5);

    if ($isMultiploThree) {
        $wordToPrint = "fizz";
    }
    if ($isMultiploFive) {
        $wordToPrint .= "buzz";
    }
    if (!$isMultiploThree && !$isMultiploFive) {
        $wordToPrint = (string) $i;
    }
    echo $wordToPrint . "\n";
    $i++;
}
function is_multiplo(int $multiplo, int $entero): bool
{
    return ($multiplo % $entero) === 0;
}
