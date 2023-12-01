<?php

/**
 * @param int $max max value for search
 * @return array|null
 */

function encuentraTriples(int $max): ?array
{
    if (!is_int($max) || $max < 3) return null;

    $numeros = range(1, $max);
    $hacerCuadrados = fn ($x) => $x * $x;
    $cuadrados = array_map($hacerCuadrados, $numeros); //tenemos un array con todos los cuadrados
    $ternas = [];

    foreach ($cuadrados as $k => $v) {
        for ($i = $k + 1; $i < count($cuadrados); $i++) {
            $suma = $v + $cuadrados[$i];
            if (in_array($suma, $cuadrados)) {
                $ternas[] = [$numeros[$k], $numeros[$i], $numeros[array_search($suma, $cuadrados)]];
            }
        }
    }
    return $ternas;
}

//Comprobacion
var_dump(encuentraTriples(10));
