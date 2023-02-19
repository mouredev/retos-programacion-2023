<?php 
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

$START = 1;
$END = 100;

function fizzbuzz($START,$END) {
    for ($i = $START; $i <= $END; $i++) {
        if ($i % (3*5) === 0) {
            echo "fizzbuzz\n";
        } else if ($i % 3 === 0) {
            echo "fizz\n";
        } else if ($i % 5 === 0) {
            echo "buzz\n";
        } else {
            echo $i."\n";
        }
    }
}

fizzbuzz($START, $END);
