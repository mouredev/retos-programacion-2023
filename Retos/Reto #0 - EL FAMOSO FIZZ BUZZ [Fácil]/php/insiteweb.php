<?php 
function NumerosFizzBuzz ($Inicio, $Final) {
    
    for ($i = $Inicio; $i <= $Final; $i++) {
        
        $valor = $i;
        if ($i % 3 == 0 && $i % 5 == 0) {
            $valor= "FIZZBUZZ";
        } elseif ($i % 3 == 0) {
            $valor= "FIZZ";
        } elseif ($i % 5 == 0) { 
            $valor= "BUZZ";
        } 
        echo $valor. "\n";
    }
}   

NumerosFizzBuzz ($Inicio, $Final);   
?>