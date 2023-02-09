<?php

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function checkNumber($num) {
    echo $num . isPrime($num) . isFibonacci($num) . evenOrOdd($num) . "\n";
}

function isPrime($num) {

    $prime = true;

    if ($num < 2) $prime = false;
    
    for($i = 2; $i <= sqrt($num); $i++) {
        if($num % $i == 0) $prime = false;
    }

    return $prime ? " es primo, " : " no es primo, ";

}

function isFibonacci($num) {
    $a = 0;
    $b = 1;
    while(true) {
        $c = $a + $b;
        if ($c == $num) return "es fibonacci ";
        if ($c > $num) return "no es fibonacci ";
        $a = $b;
        $b = $c;
    }
}

function evenOrOdd($num) {
    if ($num % 2 == 0) {
        return "y es par.";
    } else {
        return "y es impar.";
    }
}

for ($i = 0; $i<= 10; $i++) {
    checkNumber($i);
}