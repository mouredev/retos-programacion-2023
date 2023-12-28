<?php
// esto funciona
/*
function triplesPitagoricosMenoresQueNumero($numero = 10) {
    for ($i = 1; $i <= $numero; $i++) {
        for ($a = 1; $a <= $numero; $a++) {
            for ($e = 1; $e <= $numero; $e++) {
                if (pow($i, 2) + pow($a, 2) === pow($e, 2) && 
                    $i < $a) {
                    echo "($i, $a, $e)";
                }
            }
        }
    }

}

triplesPitagoricosMenoresQueNumero();

echo "<br />";

triplesPitagoricosMenoresQueNumero(30);
*/

$numero = 20;

$c = range(1, $numero);

function getTriplesPitagoricos($numero, $array) {
    array_map(function($numero2) use ($numero, $array) {
        array_map(function($numero3) use ($numero, $numero2) {
            if (pow($numero, 2) + pow($numero2, 2) === pow($numero3, 2) && 
                $numero < $numero2) {
                    echo "($numero, $numero2, $numero3)";
                }
        }, $array);
    }, $array);
}

array_map('getTriplesPitagoricos', $c, array_fill(0, $numero, $c));
