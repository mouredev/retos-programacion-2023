<?php
# Reto #4: PRIMO, FIBONACCI Y PAR
#### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23

## Enunciado
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */


function fibonacci($len)
{
    $fibonnaci = [];
    $i = 0;
    $suma = 1;
    $con = 2;
    while ($i < $len){
        $suma += $i;
        $i += $suma;
        if($i == $len || $suma == $len){
            return "Es fibonacci";
        }
    }
    return "No es fibonacci";
}

function par($len){
    if($len % 2 == 0){
        return "Es par";
    }
    return "No es par";
}

function primo($len){
    $con = 0;
    for($i = 1; $i <= $len ; $i++){
        if($len % $i == 0){
            $con++;
            if($con > 2){
                return "No es primo";
            }
        }
    }
    return "Si es primo";
}

$num = 13;
echo "<b>El numero $num</b> <br>" . fibonacci($num) . ",  " . par($num) . ", " . primo($num);