<?php
/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */

function steps(int $num): string
{
    $result = "";

    if ($num===0) {
        $result = '__';
    } else {
        $level = $num;
        if ($num > 0) {
            $result = str_repeat("  ", $num+1) . "_\n";
            while ($level>0) {
                $result .= str_repeat("  ", $level) . '_|' . "\n";
                $level--;
            }
        } else {
            $result = "_\n";
            while ($level<0) {
                $result .= " " . str_repeat("  ", $level-$num) . '|_' . "\n";
                $level++;
            }
           
        }
    }

    return $result;
}

$answer = 's';

do {
    $word = readline('Pon número de escalones: ');
    print(steps($word) . "\n\n");
    $answer = readline("¿Otra ronda (s/n) ");
} while ($answer == 's');
