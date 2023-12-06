#!/usr/bin/env raku
#`(
    La espiral
    
    Crea una función que dibuje una espiral como la del ejemplo.
    - Únicamente se indica de forma dinámica el tamaño del lado.
    - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
    
    Ejemplo: espiral de lado 5 (5 filas y 5 columnas):
    ════╗
    ╔══╗║
    ║╔╗║║
    ║╚═╝║
    ╚═══╝
    
    Joaquín Ferrero, 20230921
)
use v6;

sub espiral($tamano) {
    my $ancho = ceiling($tamano/2);

    say '=' x ($tamano-1), '╗';

    for 1 ..^ $ancho {
        say '║' x ($_-1), '╔', ('=' x ($tamano - 2*$_ - 1)), '╗', ('║' x $_);
    }

    for $ancho ..^ $tamano {
        say '║' x ($tamano - $_-1), '╚', '=' x (2*$_ - $tamano), '╝', '║' x ($tamano - $_-1);
    }
}

espiral(10);

