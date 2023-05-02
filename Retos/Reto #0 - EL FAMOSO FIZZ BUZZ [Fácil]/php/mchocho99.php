<?php
function reto0() {
    /*
    * Escribe un programa que muestre por consola (con un print) los
    * números de 1 a 100 (ambos incluidos y con un salto de línea entre
    * cada impresión), sustituyendo los siguientes:
    * - Múltiplos de 3 por la palabra "fizz".
    * - Múltiplos de 5 por la palabra "buzz".
    * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
    */
    for ($i = 1; $i <= 100; $i++ ) {
        $return = "";
        if ($i % 3 === 0) {
            $return .= "fizz";
        }
        if ($i % 5 === 0) {
            $return .= "buzz";
        }
        if ($return === "") {
            echo $i;
            echo "<br>";
        } else {
            echo $return;
            echo "<br>";
        }
    }
}

reto0();
