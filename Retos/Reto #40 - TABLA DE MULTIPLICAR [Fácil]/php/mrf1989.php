<?php
echo "Introduce un número entero para obtener su tabla de multiplicar: ";
$handle = fopen("php://stdin", "r");

$line = fgets($handle);
$number = intval(trim($line));

$factor = 1;
echo "-----------------------------\n";
echo "  TABLA DE MULTIPLICAR DE {$number} \n";
echo "-----------------------------\n";
while ($factor <= 10) {
    $product = $number * $factor;
    echo "\t{$number} x {$factor}\t= {$product}\n";
    $factor++;
}