<?php

/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

// Pseudogenerador genérico
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

// Probamos según parámetros fijos del ejemplo
for ($i=1; $i<=20; $i++) {
    printf("Vuelta %d. Resultado: %d\n", $i, myRandom(0, 100));
}

// Probamos a generar números en otros rangos
$result = 0;
for ($i=1; $i<=20; $i++) {
    $first = myRandom(0, 100);
    $last = myRandom($result, 100);
    $result = myRandom($first, $last);
    printf("Entre %d y %d. Resultado: %d\n", $first, $last, $result);
}
