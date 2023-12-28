<?php

declare(strict_types=1);

function random(): int
{
    return hrtime(true) % 101;
}

// Main code
for ($i = 0; $i < 10; $i++) {
    echo 'Random number: ' . random() . PHP_EOL;
}
