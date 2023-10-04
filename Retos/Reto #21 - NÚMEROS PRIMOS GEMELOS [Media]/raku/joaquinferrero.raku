#!/usr/bin/env raku
#`(
    Números primos gemelos
    
    Crea un programa que encuentre y muestre todos los pares de números primos
    gemelos en un rango concreto.
    
    El programa recibirá el rango máximo como número entero positivo.
    
    Un par de números primos se considera gemelo si la diferencia entre
    ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
    
    Ejemplo: Rango 14
    (3, 5), (5, 7), (11, 13)
    
    Joaquín Ferrero, 20230919
)
use v6;

my $rango = prompt "Introduce el rango a buscar primos gemelos: ";

(3 .. $rango-2).grep({ $_.is-prime and is-prime($_ + 2) }).map({ "($_, {$_+2})" }).join(", ").say;

