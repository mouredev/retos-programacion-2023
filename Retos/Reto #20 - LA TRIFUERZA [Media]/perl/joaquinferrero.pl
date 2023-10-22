#!/usr/bin/env perl
#
# La Trifuerza
#
# Crea un programa que dibuje una Trifuerza de "Zelda"
# formada por asteriscos.
# - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
# - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
#
# Ejemplo: Trifuerza 2
#
#    *
#   ***
#  *   *
# *** ***
#
# Joaquín Ferrero, 20230919
#
use v5.10;
use utf8;

@ARGV == 1 or die "Uso: $0 <n>\n";

my $trifuerza = 0+ shift;

for my $triángulo (1, 2) {
    for my $i (0 .. $trifuerza-1) {
        say ' ' x ($trifuerza*(3 - $triángulo) - $i - 1), join(' ' x ($trifuerza*2 - $i*2 - 1), ('*' x ($i*2 + 1)) x $triángulo);
    }
}

