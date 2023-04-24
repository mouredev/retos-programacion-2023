<?php
function CheckNumber($number){
    $isPrime = isPrimeNumber($number) ? "es primo, " : "no es primo, ";
    $isEven = isEvenNumber($number) ? "es par y " : "no es par y ";
    $isFibonacci = isFibonacciNumber($number) ? "es un numero de Fibonacci" : "no es numero de Fibonacci";
    return $number . " " . $isPrime . $isEven . $isFibonacci . "\n";
}

function isPrimeNumber($number){
    $isPrime = true;
    for($i = 2; $i < $number; $i++){
        if($number % $i == 0){
            $isPrime = false;
            break;
        }
    }
    return $isPrime;
}

function isEvenNumber($number){
    return $number % 2 == 0;
}

function isFibonacciNumber($number){
    $isFibonacci = false;
    $a = 0;
    $b = 1;
    while($a <= $number){
        if($a == $number){
            $isFibonacci = true;
            break;
        }
        $c = $a + $b;
        $a = $b;
        $b = $c;
    }
    return $isFibonacci;
}
echo CheckNumber(1);
echo CheckNumber(2);
echo CheckNumber(3);
echo CheckNumber(4);
echo CheckNumber(5);
echo CheckNumber(6);
echo CheckNumber(7);
echo CheckNumber(8);
echo CheckNumber(9);
echo CheckNumber(10);
echo CheckNumber(1024);
echo CheckNumber(358742586);
?>