#!/usr/bin/env perl
#
# La espiral
#
# Crea una función que dibuje una espiral como la del ejemplo.
# - Únicamente se indica de forma dinámica el tamaño del lado.
# - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
#
# Ejemplo: espiral de lado 5 (5 filas y 5 columnas):
# ════╗
# ╔══╗║
# ║╔╗║║
# ║╚═╝║
# ╚═══╝
#
# Joaquín Ferrero, 20230921
#
use v5.38;

sub espiral($tamano) {
    my $ancho = int $tamano/2+0.5;

    say '=' x ($tamano-1), '╗';

    for my $i (1 .. $ancho-1) {
        say '║' x ($i-1), '╔', '=' x ($tamano - (2 * $i) - 1), '╗', '║' x $i;
    }

    for my $i ($ancho .. $tamano-1) {
        say '║' x ($tamano - $i-1), '╚', '=' x ((2 * $i) - $tamano), '╝', '║' x ($tamano - $i-1);
    }
}

espiral(10);

__END__
