<?php

declare(strict_types=1);

function fizzbuzz(int $number): string
{
    if ($number % 3 == 0) {
        return ($number % 5 == 0) ? "fizzbuzz" : "fizz";
    }

    return ($number % 5 == 0) ? "buzz" : "{$number}";
}

// Main code
for ($i = 1; $i <= 100; $i++) {
    echo fizzbuzz($i) . "\n";
}
