<?php

/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

function baseconvert($num, $base): string
{
    $chars = "0123456789ABCDEF";
    $result = "";

    while ($num > 0) {
        $mod = $num % $base;
        $result = $chars[$mod] . $result;
        $num = intval($num / $base);
    }

    return $result;
}

function to8($num): string
{
    return baseconvert($num, 8);
}

function to16($num): string
{
    return baseconvert($num, 16);
}

$numbers = [ 4, 10, 30, 45, 100, 1000];

foreach($numbers as $number) {
    printf("El número %d en octal es %s\n", $number, to8($number));
    printf("El número %d en hexadecimal es %s\n", $number, to16($number));
}
