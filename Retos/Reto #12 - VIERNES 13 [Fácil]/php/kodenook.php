<?php

declare(strict_types=1);

function friday13(int $month = 12, int $year = 12): bool
{
    $day = date('N', strtotime("$year/$month/13"));

    if ((int)$day === 5) return true;

    return false;
}

echo friday13(8, 2023), PHP_EOL;
echo friday13(10, 2023), PHP_EOL;
