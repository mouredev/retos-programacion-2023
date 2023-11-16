<?php
/* Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

    function esMultiplo($num, $multi){

        return $num % $multi == 0; //si al dividir el número pasado por parámetro y el número del que queremos buscar el divisor nos da cero, el resto es cero, significa que el número es divisor y, por lo tanto, también múltiplo, por lo que devolverá verdadero.

    }

    $long = 100;

    for($i=1;$i<=$long;$i++){
        
        switch(true){
            case (esMultiplo($i,3) && esMultiplo($i,5)) :
                echo "fizzbuzz<br>";
                break;
            case (esMultiplo($i,3)) :
                echo "fizz<br>";
                break;
            case (esMultiplo($i,5)) :
                echo "buzz<br>";
                break;
            default:
                echo $i . "<br>";
                break;
        }

    }



?>