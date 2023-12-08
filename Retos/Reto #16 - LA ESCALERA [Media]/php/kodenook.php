<?php
declare (strict_types = 1);

function stairs(int $steps): string
{
    $stair;
    if ($steps < 0) {
        $stair = '_' . PHP_EOL . ' ';
        for ($i = 0; $i > $steps; $i--) {
            $stair .= str_repeat('  ', $i * -1) . '|_' . PHP_EOL;
        }

    } elseif ($steps > 0) {
        $stair = str_repeat('  ', $steps) . '_' . PHP_EOL;
        for ($i = 0; $i < $steps; $i++) {
            $stair .= str_repeat('  ', $steps - $i - 1) . '_|' . PHP_EOL;
        }

    } else {
        $stair = '__';
    }

    return $stair . PHP_EOL;
}

echo stairs(6);
echo stairs(0);
echo stairs(-5);
