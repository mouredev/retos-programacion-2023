<?php
function generarClave($longitud = 8, $mayusculas = false, $numeros = false, $especiales = false){
    
    if ($longitud < 8 || $longitud > 16){
        echo "El numero de caracteres esta fuera del rango 8-16\n";
        return;
    }
    
    $clave ="";
    
    $cadena = "abcdefghijklmnopqrstuvwxyz";

    if ($mayusculas) {
        $cadena .= "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    }

    if ($numeros) {
        $cadena .= "1234567890";
    }

    if ($especiales) { 
        $cadena .= "|@#~$%()=^*+[]{}-_"; 
    }

    for($i=0;$i<$longitud;$i++) { 
        $clave .= substr($cadena,rand(0,strlen($cadena)-1),1); 
    }

    echo $clave . "\n";
}

generarClave();
generarClave(10, true, true, true);
generarClave(15, false, true, false);
generarClave(9, true, false, false);
generarClave(3);
generarClave(21);
?>