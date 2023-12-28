<?php

    function esPrimo ($num)
    {
        if($num == 1) return false;
        
        for($i=2; $i<=sqrt($num); $i++) {
            if($num % $i == 0) return false;
        }

        return true;
    }

    function esFibonacci ($num) 
    {
        $a = 0;
        $b = 1;

        while ($b < $num) {
            $temp = $a;
            $a = $b;
            $b = $temp + $b;
        }

        return $b == $num;
    }

    function esPar($num) {
        return $num % 2 == 0;
    }

    function comprobarNumero ($num)
    {
        $mensaje = "El numero $num ";

        $mensaje .= esPrimo($num) ? "es primo, " : "no es primo, ";

        $mensaje .= esFibonacci($num) ? "es fibonacci, " : "no es fibonacci, ";

        $mensaje .= esPar($num) ? "y es par" : "y es impar";

        echo $mensaje."\n";
    }

    for($i = 1; $i < 10; $i++){
        comprobarNumero($i);
    }
?>