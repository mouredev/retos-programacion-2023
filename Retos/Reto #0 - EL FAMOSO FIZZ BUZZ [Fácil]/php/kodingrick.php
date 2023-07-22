<?php

declare(strict_types=1);

/**
 * The function fizzbuzz prints numbers from 1 to 100, replacing multiples of 3 with "fizz", multiples
 * of 5 with "buzz", and multiples of both 3 and 5 with "fizzbuzz".
 */
function fizzbuzz(): void
{
    foreach (range(1, 100) as $number) {
        if (fmod($number, 3) == 0 && fmod($number, 5) == 0) {
            echo 'fizzbuzz' . PHP_EOL;
        } elseif (fmod($number, 3) == 0) {
            echo 'fizz' . PHP_EOL;
        } elseif (fmod($number, 5) == 0) {
            echo 'buzz' . PHP_EOL;
        } else echo $number . PHP_EOL;
    }
}

fizzbuzz();
