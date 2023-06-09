<?php

/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

// Pseudogenerador genérico 1
function myRandom($first, $last)
{
    // Si $last es menor que $first, los intercambiamos
    if ($last<$first) {
        $x = $first;
        $first = $last;
        $last = $x;
    }
    $d=new DateTime();
    return ($d->format('u') % ($last-($first-1))) + $first;
}

// Pseudogenerador genérico 2
function myRandom2($first, $last)
{
    // Si $last es menor que $first, los intercambiamos
    if ($last<$first) {
        $x = $first;
        $first = $last;
        $last = $x;
    }
    $max = 50;
    $d1 = 0;
    $d=new DateTime();
    // Añadimos un poco de complejidad para reducir las posibilidades de repetir
    for ($times=1; $times < $max; $times++) {
        for ($i=0; $i<strlen($d->format('u')); $i++) {
            $d1 += $d->format('u')[$i];
            $d1 += ($d1 * 3) % $last;
        }
    }

    return ($d1 % ($last-($first-1))) + $first;
}

$r0 = [];
// Probamos según parámetros fijos del ejemplo
for ($i=1; $i<=100; $i++) {
    $result= myRandom(0, 100);
    if (empty($r0[$result])) {
        $r0[$result] = 0;
    }
    $r0[$result]++;
    #printf("Vuelta %d. Resultado: %d\n", $i, $result);
}


$r1 = []; //Para almacenar los resultados y analizarlos
for ($i=1; $i<=100; $i++) {
    $first = 0; //myRandom2(0, 100);
    $last = 100; //myRandom2($result, 100);
    $result = myRandom2($first, $last);
    $result = rand($first, $last);
    if (empty($r1[$result])) {
        $r1[$result] = 0;
    }
    $r1[$result]++;
}

// Analisis de resultados
foreach ($r0 as $k => $v) {
    #printf("%d ha salido %d veces\n", $k, $v);
}
printf("Total: %d numeros diferentes.\n", count($r0));
foreach ($r1 as $k => $v) {
    #printf("%d ha salido %d veces\n", $k, $v);
}

printf("Total: %d numeros diferentes.\n", count($r1));
