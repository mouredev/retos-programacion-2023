<?php

/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

function myRandom()
{
    $d=new DateTime();
    return $d->format('u') % 101;
}

for ($i=1; $i<=20; $i++) {
    printf("Vuelta %d. Resultado: %d\n", $i, myRandom());
}
