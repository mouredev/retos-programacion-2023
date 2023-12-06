<?php

function comparador($cadena1, $cadena2) {
    $encontrados = [];
    $contador = 0;
    
    for($i = 0; $i < strlen($cadena1); $i++){
        if($cadena1[$i] != $cadena2[$i]){
            $encontrados[$contador] = $cadena2[$i];
            $contador++;
        }
    }
    return $encontrados;
}
 
print_r(comparador('Me llamo mouredev', 'Me llemo mouredov'));
print_r(comparador('Me llamo.Brais Moure', 'Me llamo brais moure'));
 
?>
