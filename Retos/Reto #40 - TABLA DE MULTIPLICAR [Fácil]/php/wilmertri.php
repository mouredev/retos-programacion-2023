<?php

/**
 * @param int $n
 * @return void
 */
function multiplicate_table(int $n): void
{
    foreach (range(1, 10) as $i)
    {
        echo "{$n} x {$i} = ".($n * $i)." \n";
    }

}

echo "Ingrese un número para imprimir su tabla de multiplicar: ";
$number = intval(fgets(STDIN));
multiplicate_table($number);