<?php

$abaco = [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"
];

// Encontrar el número
$num = [];
array_walk($abaco, function ($elem) use (&$num) {
    $num[] = strpos($elem, '-');
});

// Devuelve el número sin separador de miles
echo implode('', $num) . PHP_EOL; // 1302790

// Agrega separador de miles
$num_sep = '';
$reversed = array_reverse($num);
array_walk($reversed, function ($char, $i) use (&$num_sep) {
    $num_sep.= $char;
    if (($i + 1) % 3 === 0) {
        $num_sep.= '.';
    }
});

echo strrev($num_sep) . PHP_EOL; // 1.302.790
