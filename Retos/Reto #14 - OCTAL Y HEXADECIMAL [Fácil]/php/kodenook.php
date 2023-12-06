<?php

declare (strict_types = 1);

/**
 * The function decimalToOctal converts a decimal number to its octal representation.
 *
 * @param int num The parameter `num` is an integer representing the decimal number that you want to
 * convert to octal.
 *
 * @return int an integer value that represents the octal conversion of the input decimal number.
 */
function decimalToOctal(int $num): int
{
    $octal = [];
    $quotient;
    $remainder;

    $remainder = intval(fmod($num, 8));
    $quotient = intval($num / 8);
    array_unshift($octal, $remainder);

    while ($quotient >= 1) {
        $remainder = intval(fmod($quotient, 8));
        $quotient = intval($quotient / 8);
        array_unshift($octal, $remainder);

    }

    $octal = implode('', $octal);

    return (int) $octal;
}

/**
 * The function converts a decimal number to its hexadecimal representation.
 *
 * @param int num The parameter `num` is an integer representing the decimal number that you want to
 * convert to hexadecimal.
 *
 * @return string a string representation of the input decimal number in hexadecimal format.
 */
function decimalToHexadecimal(int $num): string
{
    $hexadecimals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];
    $hexadecimal = [];
    $quotient;
    $remainder;

    $remainder = intval(fmod($num, 16));
    $quotient = intval($num / 16);
    array_unshift($hexadecimal, $hexadecimals[$remainder]);

    while ($quotient >= 1) {
        $remainder = intval(fmod($quotient, 16));
        $quotient = intval($quotient / 16);
        array_unshift($hexadecimal, $hexadecimals[$remainder]);

    }

    $hexadecimal = implode('', $hexadecimal);

    return $hexadecimal;
}

/**
 * The function decimalToOctalHexadecimal takes an integer as input and prints its octal and
 * hexadecimal representations.
 *
 * @param int num The parameter "num" is an integer representing the decimal number that you want to
 * convert to octal and hexadecimal.
 */
function decimalToOctalHexadecimal(int $num): void
{
    echo 'octal: ' . decimalToOctal($num), PHP_EOL;
    echo 'hexadecimal: ' . decimalToHexadecimal($num), PHP_EOL;
}

decimalToOctalHexadecimal(127);
decimalToOctalHexadecimal(255);
