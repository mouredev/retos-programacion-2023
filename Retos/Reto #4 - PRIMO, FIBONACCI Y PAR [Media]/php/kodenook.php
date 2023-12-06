<?php

declare(strict_types=1);

/**
 * The function checks if a given number is prime or not.
 * 
 * @param int num The parameter "num" is an integer that represents the number we want to check if it
 * is prime or not.
 * 
 * @return string The function isPrime is returning a string indicating whether the given number is
 * prime or not. If the number is less than or equal to 1, the function returns 'no es primo' (not
 * prime). If the number is greater than 1 and is not divisible by any number other than 1 and itself,
 * the function returns 'es primo' (is prime).
 */
function isPrime(int $num): string
{
    if ($num <= 1) return 'no es primo';

    for ($i = 2; $i <= (int)sqrt($num); $i++) {
        if (fmod($num, $i) === 0.0) return 'no es primo';
    }

    return 'es primo';
}

/**
 * The function checks if a given number is a Fibonacci number or not.
 * 
 * @param int num The parameter "num" is an integer that represents the number we want to check if it
 * is a Fibonacci number or not.
 * 
 * @return string a string indicating whether the given number is a Fibonacci number or not. If the
 * number is a Fibonacci number, the function returns the string 'es fibonacci'. If the number is not a
 * Fibonacci number, the function returns the string 'no es fibonacci'.
 */
function isFibonacci(int $num): string
{
    $last = 0;
    $actual = 1;

    while ($actual < $num) {
        $sum = $last + $actual;

        if ($sum === $num) return 'es fibonacci';

        $last = $actual;
        $actual = $sum;
    }

    return 'no es fibonacci';
}

/**
 * The function checks if a given number is even or odd and returns a string indicating the result.
 * 
 * @param int num The parameter "num" is an integer that represents the number we want to check if it
 * is even or odd.
 * 
 * @return string a string that indicates whether the given number is even or odd. If the number is
 * even, the function returns the string 'es par'. If the number is odd, the function returns the
 * string 'es impar'.
 */
function isEven(int $num): string
{
    if (fmod($num, 2) === 0.0) return 'es par';

    return 'es impar';
}


/**
 * The function takes an integer as input and returns a string that includes whether the number is
 * prime, Fibonacci, and even.
 * 
 * @param int num The parameter "num" is an integer that represents a number.
 * 
 * @return string a formatted string that includes the input number, whether it is prime or not,
 * whether it is a Fibonacci number or not, and whether it is even or not.
 */
function analyze(int $num): string
{
    return sprintf('%d %s, %s y %s', $num, isPrime($num), isFibonacci($num), isEven($num)) . PHP_EOL;
}

echo analyze(2);
echo analyze(7);
