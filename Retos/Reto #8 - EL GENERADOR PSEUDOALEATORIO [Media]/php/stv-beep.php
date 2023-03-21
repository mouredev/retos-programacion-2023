<?php

/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

function myRandom() {
    $t = hrtime(true);
    return $t % 101;
}

printf(myRandom());
