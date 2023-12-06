<?php
$seed = round(microtime(true) * 1000);

$randomizer = function($a, $m) use (&$seed) {
    $q = intval($m / $a);
    $r = $m % $a;

    $seed = $a * ($seed % $q) - $r * intval($seed / $q);

    if ($seed <= 0) {
        $seed += $m;
    }

    return $seed;
};

echo "Cuantos numeros quieres generar?: ";
fscanf(STDIN, "%s", $contador);
$a = round(microtime(true) * 1000);
$m = round(microtime(true) * 10000);

for ($i = 0; $i < $contador; $i++) {
    $random_number = abs(1 + $randomizer($a, $m) % 100);
    echo "Número aleatorio " .($i+1)." generado: "  .$random_number . "\n";
    sleep(3);
}
?>