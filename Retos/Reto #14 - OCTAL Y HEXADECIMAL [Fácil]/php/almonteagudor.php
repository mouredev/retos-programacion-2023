<?php

function decimalConverter(int $decimal, int $base): string
{
    $relation = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"];

    $quotient = floor($decimal / $base);
    $remainder = $decimal % $base;

    if ($quotient > ($base - 1)) {
        $quotient = decimalConverter($quotient, $base);
    }

    return $quotient . $relation[$remainder];
}

function decimalToOctal(int $decimal): string
{
    return decimalConverter($decimal, 8);
}

function decimalToHexadecimal(int $decimal): string
{
    return decimalConverter($decimal, 16);
}

foreach (range(0, 100) as $decimal) {
    echo $decimal . " = " . decimalToOctal($decimal) . "\n";
}

foreach (range(0, 100) as $decimal) {
    echo $decimal . " = " . decimalToHexadecimal($decimal) . "\n";
}
