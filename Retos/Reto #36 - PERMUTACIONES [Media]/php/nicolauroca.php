<?php

/**
 * Genera e imprime todas las permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso
 *
 * @param   string  $palabra            La palabra para la cual se generarán las permutaciones.
 * @param   int     $inicio (Opcional)  El índice de inicio para la generación de permutaciones.
 * @return  array                       Un arreglo que contiene todas las permutaciones únicas de la palabra de entrada.
 */

function permutaciones($palabra, $inicio = 0) {
    
    // Verificamos si la palabra es una cadena (si no, la convertimos a arreglo)
    if (!is_array($palabra)) {
        $palabra = str_split($palabra);
    }

    // Preparamos la salida como un conjunto (array) para garantizar permutaciones únicas
    $salida = [];

    // Jugamos con la longitud restante para saber si añadimos o continuamos con la recursión
    if ($inicio == count($palabra) - 1) {
        $salida[] = implode('', $palabra);
    } else {
        for ($i = $inicio; $i < count($palabra); $i++) {
            // Jugamos por elemento (letra) de la palabra
            [$palabra[$inicio], $palabra[$i]] = [$palabra[$i], $palabra[$inicio]];

            // Utilizamos la recursión para generar permutaciones
            $salida = array_merge($salida, permutaciones($palabra, $inicio + 1));

            // Dejamos el texto como estaba
            [$palabra[$inicio], $palabra[$i]] = [$palabra[$i], $palabra[$inicio]];
        }
    }

    return array_unique($salida);
}

// Ejemplo de uso
$permutaciones = permutaciones('sol');

foreach ($permutaciones as $permutacion) {
    echo $permutacion . "\n";
}

?>