<?php
# Reto #0: EL FAMOSO "FIZZ BUZZ"
#### Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23

## Enunciado

/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

for ($i = 1; $i <= 100; $i++) {
    echo getMultiple($i) . "\n";
}

function getMultiple($num)
{
    if ($num % 3 == 0 && $num % 5 == 0) {
        return $num . " FIZZBUZZ";
    }

    if ($num % 3 == 0) {
        return $num . " FIZZ";
    }

    if ($num % 5 == 0) {
        return $num . " BUZZ";
    }

    return $num;
}
