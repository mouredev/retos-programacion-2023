<?php

declare(strict_types=1);

function generatePassword(
    int $length = 12,
    bool $upper = false,
    bool $numbers = false,
    bool $symbols = false,
): string {
    $pattern = 'abcdefghijklmnopqrstuvwxyz';

    $length = filter_var($length, FILTER_VALIDATE_INT, [
        'options' => [
            'default' => 12,
            'min_range' => 8,
            'max_range' => 16,
        ],
    ]);

    if ($upper) {
        $pattern .= strtoupper($pattern);
    }

    if ($numbers) {
        $pattern .= '0123456789';
    }

    if ($symbols) {
        $pattern .= '~!@#$%^&*()-_=+[]{};:?';
    }

    return substr(str_shuffle($pattern), 0, $length);
}

// Main code
echo generatePassword() . "\n";
echo generatePassword(8, symbols: true) . "\n";
echo generatePassword(16, upper: true) . "\n";
echo generatePassword(20, numbers: true) . "\n";
echo generatePassword(numbers: true, symbols: true) . "\n";
echo generatePassword(16, upper: true, numbers: true, symbols: true) . "\n";
