<?php

declare(strict_types=1);

/**
 * The function fizzbuzz takes a start and end number as input and prints "fizz" if the number is
 * divisible by 3, "buzz" if the number is divisible by 5, "fizzbuzz" if the number is divisible by
 * both 3 and 5, and the number itself if none of the conditions are met.
 * 
 * @param int start The start parameter is the starting number for the fizzbuzz sequence. It determines
 * where the sequence will begin.
 * @param int end The "end" parameter is the last number in the range of numbers for which the FizzBuzz
 * game will be played.
 */
function fizzbuzz(int $start, int $end): void
{
    foreach (range($start, $end) as $num) {
        if (fmod($num, 3) === 0.0 && fmod($num, 5) === 0.0) {
            echo 'fizzbuzz', PHP_EOL;
        } elseif (fmod($num, 3) === 0.0) {
            echo 'fizz', PHP_EOL;
        } elseif (fmod($num, 5) === 0.0) {
            echo 'buzz', PHP_EOL;
        } else {
            echo $num, PHP_EOL;
        }
    }
}

fizzbuzz(1, 100);
