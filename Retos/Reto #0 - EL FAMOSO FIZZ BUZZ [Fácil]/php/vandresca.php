<?php

/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */


for($i=1; $i<=100; $i++){
    println(fizz_buzz($i));
}

function fizz_buzz($number){
    if($number%15==0) return "fizzbuzz";
    if($number%5==0) return "buzz";
    if($number%3==0) return "fizz";
    return $number;
}

function println($text){
    echo $text."\n";
}