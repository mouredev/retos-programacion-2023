<?php

/*
 * Función que calcula el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

echo calcValorExcel('A') . PHP_EOL; // 1
echo calcValorExcel('Z') . PHP_EOL; // 26
echo calcValorExcel('AA') . PHP_EOL; // 27
echo calcValorExcel('CA') . PHP_EOL; // 79
echo calcValorExcel('EE') . PHP_EOL; // 135

function calcValorExcel(string $excel): int
{
    $valores = [];
    foreach(array_reverse(str_split($excel)) as $index => $letter) {
        $char = ord($letter) - 64;
        $valores[] = ($index === 0) ? $char : $char * 26;
    }
    return array_sum($valores);
}
