#!/usr/bin/env raku
#`(
    Colores HEX y RGB
    
    Crea las funciones capaces de transformar colores HEX a RGB y viceversa.
    
    Ejemplos:
      RGB a HEX: r: 0, g: 0, b: 0 -> #000000
      HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
    
    Joaquín Ferrero, 20230919
)
use v6;

sub HEXtoRGB($HEX) { $HEX.substr(1).comb(2)».parse-base(16) }
sub RGBtoHEX(+@RGB) { '#' ~ @RGB.map({.base(16)}).join }

"(r: %d, g: %d, b: %d)".sprintf( HEXtoRGB('#C21A4D') ).say;
say RGBtoHEX(194, 26, 77);

