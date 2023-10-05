<?php

$triples = [];

function encontrar_numeros_pitagoricos($n) {


    for($a = 1; $a <= $n; $a++) {
        for($b = $a; $b <= $n; $b++) {
            $c = sqrt($a * $a + $b * $b);
            if(is_int($c) && $c <= $n) {
                $triples[] = array($a, $b, (int)$c);
            }
        }
    }

    return $triples;


    echo "Introduce un número para buscar sus Triples Pitagóricos: ";
    $numero_limite = intval(fgets(STDIN));
    $triples_pitagoricos = encontrar_numeros_pitagoricos($numero_limite);

    echo "Triples Pitagóricos menos o iguales a $numero_limite\n";

    foreach ($triples_pitagoricos as $triple) {
        echo implode(", ", $triple) . "\n";
    }



}

encontrar_numeros_pitagoricos(20);


