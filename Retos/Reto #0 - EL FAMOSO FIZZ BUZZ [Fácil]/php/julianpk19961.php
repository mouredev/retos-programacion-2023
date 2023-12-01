<?php

/*
    Escribe un programa que muestre por consola (con un print)
    los números del 1 al 100 [ambos incluidos y con un salto de línea en cada impresión]
    Sustituyendo lo siguiente:
        Multiplos de 3 por la palabra Fizz
        Multiplos de 5 por la palabra Buzz
        Multiplos de 3 y 5 por la palabra FizBuzz
*/

function FizBuzz(int $inicio, int $fin)
{

    for ($i = $inicio; $i <= $fin; $i++) {

        if ($i % 3 == 0 && $i % 5 == 0) {
            // Multiplos de 3 & 5
            echo 'FizzBuzz' . "\n";
        } elseif ($i % 5 == 0) {
            // Multiplos de 5
            echo 'Buzz' . "\n";
        } elseif ($i % 3 == 0) {
            // Multiplos de 3
            echo 'Fizz' . "\n";
        } else {
            // Excepciones
            echo $i . "\n";
        }
    }
}

// Captura de datos
$inicio = readline('Ingrese el número inicial del ciclo: ');
$fin = readline('Ingrese el número final del ciclo: ');

// Conversión a Enteros
$inicio = filter_var($inicio, FILTER_VALIDATE_INT);
$fin = filter_var($fin, FILTER_VALIDATE_INT);

// Validaciones de entrada
if (!is_int($inicio) || !is_int($fin)) {
    echo "Uno o más números no son validos";
} elseif ($fin < $inicio) {
    echo "El número final no puede ser menor al número inicial";
} else {
    echo FizBuzz($inicio, $fin);
}
