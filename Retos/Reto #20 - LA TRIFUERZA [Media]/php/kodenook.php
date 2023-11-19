<?php

declare (strict_types = 1);

/**
 * The `triforce` function in PHP prints a pattern resembling a triforce shape using asterisks and.
 *
 * @param int lines The parameter "lines" represents the number of lines in the triforce pattern.
 */
function triforce(int $lines): void
{
    for ($i = 1; $i <= $lines; $i++) {
        echo str_repeat(' ', $lines);
        echo str_repeat(' ', $lines - $i) . str_repeat('*', 2 * $i - 1) . str_repeat(' ', $lines - $i), PHP_EOL;
    }
    for ($i = 1; $i <= $lines; $i++) {
        echo str_repeat(' ', $lines - $i) . str_repeat('*', 2 * $i - 1) . str_repeat(' ', $lines - $i);
        echo str_repeat(' ', 1);
        echo str_repeat(' ', $lines - $i) . str_repeat('*', 2 * $i - 1) . str_repeat(' ', $lines - $i), PHP_EOL;
    }

}

triforce(5);
