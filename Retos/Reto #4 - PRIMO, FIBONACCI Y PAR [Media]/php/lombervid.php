<?php

declare(strict_types=1);

function isEven(int $num): bool
{
    return $num % 2 == 0;
}

function isPrime(int $num): bool
{
    if ($num == 2 || $num == 3) {
        return true;
    }

    if ($num <= 1 || isEven($num) || $num % 3 == 0) {
        return false;
    }

    for ($i = 5; $i <= sqrt($num); $i += 6) {
        if ($num % $i == 0 || $num % ($i + 2) == 0) {
            return false;
        }
    }

    return true;
}

function isPerfectSquare(int $num): bool
{
    $sqrt = intval(sqrt($num));

    return $num == pow($sqrt, 2);
}

function isFibonacci(int $num): bool
{
    if ($num < 0) {
        return false;
    }

    return isPerfectSquare(5 * $num * $num + 4) || isPerfectSquare(5 * $num * $num - 4);
}

function evaluateNumber(int $num): string
{
    $noPrime = !isPrime($num) ? 'no ' : '';
    $noFibon = !isFibonacci($num) ? 'no ' : '';
    $evenOrOdd = isEven($num) ? 'par' : 'impar';

    return "{$num} {$noPrime}es primo, {$noFibon}es fibonacci y es {$evenOrOdd}";
}

// Test cases
// $failed = 0;
// $tests = [
//     [-29, '-29 no es primo, no es fibonacci y es impar'],
//     [-1, '-1 no es primo, no es fibonacci y es impar'],
//     [0, '0 no es primo, es fibonacci y es par'],
//     [2, '2 es primo, es fibonacci y es par'],
//     [3, '3 es primo, es fibonacci y es impar'],
//     [5, '5 es primo, es fibonacci y es impar'],
//     [8, '8 no es primo, es fibonacci y es par'],
//     [107, '107 es primo, no es fibonacci y es impar'],
//     [144, '144 no es primo, es fibonacci y es par'],
//     [854, '854 no es primo, no es fibonacci y es par'],
//     [5867, '5867 es primo, no es fibonacci y es impar'],
//     [28657, '28657 es primo, es fibonacci y es impar'],
// ];

// foreach ($tests as [$num, $want]) {
//     $got = evaluateNumber($num);

//     if ($got != $want) {
//         $failed++;
//         echo "Test failed:\n\tnum: {$num}\n\tgot: {$got}\n\twant: {$want}\n\n";
//     }
// }

// if (!$failed) {
//     echo "All tests passed" . PHP_EOL;
// }
