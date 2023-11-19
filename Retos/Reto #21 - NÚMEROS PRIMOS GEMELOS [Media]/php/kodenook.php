<?php

declare (strict_types = 1);

/**
 * The function checks if a given number is prime or not.
 *
 * @param int num The parameter "num" is an integer that represents the number we want to check if it
 * is prime or not.
 *
 * @return bool a boolean value, either true or false.
 */
function isPrime(int $num): bool
{
    if ($num <= 1) {
        return false;
    }

    for ($i = 2; $i <= (int) sqrt($num); $i++) {
        if (fmod($num, $i) === 0.0) {
            return false;
        }
    }

    return true;
}

/**
 * The function "primeTwins" returns a string containing pairs of prime numbers that are two units
 * apart, up to a given maximum number.
 *
 * @param int numMax The parameter `numMax` represents the maximum number up to which we want to find
 * prime twin pairs.
 *
 * @return string a string that contains pairs of prime numbers that are twin primes. Each pair is
 * enclosed in parentheses and separated by a comma.
 */
function primeTwins(int $numMax): string
{
    $numbers = [];
    $response = '';

    for ($i = 0; $i <= $numMax; $i++) {
        if (isPrime($i)) {
            array_push($numbers, $i);
        }
    }

    for ($i = 0; $i < count($numbers); $i++) {
        if ($i + 1 >= count($numbers)) {
            continue;
        }

        if ($numbers[$i + 1] - $numbers[$i] === 2) {
            $response .= '(' . $numbers[$i] . ',' . $numbers[$i + 1] . ') ';
        }
    }

    return $response;
}

echo primeTwins(14) . PHP_EOL;
echo primeTwins(7) . PHP_EOL;
echo primeTwins(2) . PHP_EOL;
