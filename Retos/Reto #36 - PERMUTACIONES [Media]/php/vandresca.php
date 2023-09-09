<?php
/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una word.
 * - Las words generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */

 function permutations($word){
    if(strlen($word)==0){
        return [""];
    }

    $permutations = array();
    $wordLength=strlen($word);
    for($i=0; $i<$wordLength; $i++){
        foreach(permutations(substr($word, 0, $i) . substr($word, $i + 1)) as $key=>$permutation) {
            $permutations[] = $word[$i] . $permutation;
          }
    }
    return $permutations;
 }
 
 function printPermutations($word){
    $permutations = permutations($word);
    foreach($permutations as $permutation){
        echo $permutation. "  ";
    }
    echo "\n";
 }
 
 printPermutations("sol");
 printPermutations("mar");
 printPermutations("cabra");

 ?>
