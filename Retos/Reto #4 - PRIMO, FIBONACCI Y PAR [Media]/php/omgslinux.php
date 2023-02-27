<?php
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

class Fibonacci
{
    private $debug;

    public function __construct($debug = false)
    {
        $this->debug = $debug;
    }

    public function checkFibonacci($number): bool
    {
        $prev = 0;
        $next = 1;
        $result = 1;
        while ($result<=$number) {
            $result = $prev + $next;
            $prev = $next;
            $next = $result;
            if ($this->debug) {
                printf("prev: %d next: %d result: %d\n", $prev, $next, $result);
            }
        }

        return $number==$prev;
    }
}

function isDivisible($number, $debug = false)
{
    $i = 2;
    $div = false;
    while ($i<($number**0.5) && (!$div)) {
        if ($debug) {
            printf("probando %d\n", $i);
        }
        if (($number % $i)==0) {
            $div = true;
        }
        $i++;
    }

    return $div;
}

$test = new Fibonacci();
$numbers = [2, 3, 4, 5, 6, 7, 8, 11, 13, 20, 33, 34, 55];
foreach ($numbers as $number) {
    $odd = $number % 2;
    // El 2 es primo
    $div = ($odd?isDivisible($number):$number!=2);
    $fibo = $test->checkFibonacci($number);
    printf("%d:%s es primo,%s fibonacci y es %s\n", $number, ($div?' no':''), ($fibo?'':' no'), ($odd?'impar':'par'));
}
