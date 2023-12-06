<?php

function abacoToNumber(array $abaco): int
{
    $number = "";

    foreach ($abaco as $unit) {
        $number .= strpos($unit, "---");
    }

    return intval($number);
}

$abaco = isset($argv[1]) ? explode(',', $argv[1]) : ["O---OOOOOOOO", "OOO---OOOOOO", "---OOOOOOOOO", "OO---OOOOOOO", "OOOOOOO---OO", "OOOOOOOOO---", "---OOOOOOOOO"];

echo "El número es " . abacoToNumber($abaco) . "\n";
