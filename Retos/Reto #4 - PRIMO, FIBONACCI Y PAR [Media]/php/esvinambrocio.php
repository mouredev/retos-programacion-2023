<?php

/**
 * Comprobar si el numero es par
 *
 * @param int $number
 * @return bool
 */
function checkIsPar(int $number): bool
{
    return ($number % 2) === 0;
}

/**
 * Comprobar si el numero es primo
 *
 * @param int $number
 * @return bool
 */
function checkIsPrime(int $number): bool
{
    if ($number < 1) {
        return false;
    }
    $numbers = range(2, $number);

    $result = true;
    foreach ($numbers as  $numberRange) {
        if (($number % $numberRange) === 0 &&
            $number !== $numberRange
        ) {
            $result = false;
            break;
        }
    }
    return $result;
}

/**
 * Comprobar si el numero es fibonacci
 *
 * @param int $number
 * @return bool
 */
function checkIsFibonacci(int $number): bool
{
    return checkIsPerfectSquare(5 * $number * $number + 4) || checkIsPerfectSquare(5 * $number * $number - 4);
}

/**
 * Comprobar si el numero es un cuadrado perfecto
 *
 * @param int $number
 * @return bool
 */
function checkIsPerfectSquare(int $number): bool
{
    $sqrt = (int) sqrt($number);
    return ($sqrt * $sqrt) === $number;
}

function checkPrimeFibonacciEven(int $number): void
{
    $par = "es impar";
    $fibonacci = "no es fibonacci";
    $prime = "no es primo";
    if (checkIsPar($number)) {
        $par = "es par";
    }
    if (checkIsFibonacci($number)) {
        $fibonacci = "es fibonacci";
    }
    if (checkIsPrime($number)) {
        $prime = "es primo";
    }

    $text = "$number $prime, $fibonacci y $par \n";
    echo $text;
}
checkPrimeFibonacciEven(2);
checkPrimeFibonacciEven(7);
checkPrimeFibonacciEven(0);
checkPrimeFibonacciEven(1);
checkPrimeFibonacciEven(-2);
