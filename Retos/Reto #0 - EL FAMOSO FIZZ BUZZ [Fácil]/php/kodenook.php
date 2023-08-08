<?php

declare(strict_types=1);

/**
 * The function fizzbuzz takes a start and end number as input and prints "fizz" if the number is
 * divisible by 3, "buzz" if the number is divisible by 5, "fizzbuzz" if the number is divisible by
 * both 3 and 5, and the number itself if none of the conditions are met.
 * 
 * @param int start The start parameter is the starting number for the fizzbuzz sequence. It determines
 * where the sequence will begin.
 * @param int end The "end" parameter is the last number in the range of values for which the FizzBuzz
 * game will be played.
 */
function fizzbuzz(int $start, int $end): void
{
    foreach (range($start, $end) as $value) {
        if (fmod($value, 3) === 0.0 && fmod($value, 5) === 0.0) {
            echo 'fizzbuzz', PHP_EOL;
        } elseif (fmod($value, 3) === 0.0) {
            echo 'fizz', PHP_EOL;
        } elseif (fmod($value, 5) === 0.0) {
            echo 'buzz', PHP_EOL;
        } else {
            echo $value, PHP_EOL;
        }
    }
}

/* The line `fizzbuzz(1, 100);` is calling the `fizzbuzz` function with the arguments `1` and `100`.
This means that the function will print the FizzBuzz sequence starting from 1 and ending at 100. */
fizzbuzz(1, 100);
