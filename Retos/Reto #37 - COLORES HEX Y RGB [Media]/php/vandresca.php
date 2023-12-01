<?php

/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */

 function pad($str){
    return str_pad($str,2,"0", STR_PAD_LEFT);
 }

function rgb_to_hex($red, $green, $blue):string{
    $hex = pad(dechex($red)) . pad(dechex($green)) . pad(dechex($blue));
    return strtoupper($hex) . "\n";
}

function hex_to_rgb($hex){
    $r = substr($hex, 0, 2);
    $g = substr($hex, 2, 2);
    $b = substr($hex, 4, 2);
    
    $rgb = array("red"=>hexdec($r), "green"=>hexdec($g), "blue"=>hexdec($b));
    return $rgb;
}


print rgb_to_hex(255, 0, 255);
print rgb_to_hex(242, 123, 55);
print rgb_to_hex(35, 23, 178);
print rgb_to_hex(100, 200, 199);


print_r(hex_to_rgb("FF00FF"));
print_r(hex_to_rgb("F27B37"));
print_r(hex_to_rgb("2317B2"));
print_r(hex_to_rgb("64C8C7"));


