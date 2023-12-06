<?php

declare(strict_types=1);

function isFriday13th($month, $year): string
{
    $date = strtotime("$year-$month-13");
    return ('5' === date('N', $date)) ? 'True' : 'False';
}

echo isFriday13th(3, 2023) . PHP_EOL;
echo isFriday13th(1, 2023);

?>