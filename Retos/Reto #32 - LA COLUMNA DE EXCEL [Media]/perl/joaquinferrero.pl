#!/usr/bin/env perl
#
# Reto #32. «La columna de Excel»
#
# Programa:
#
#   Crea una función que calcule el número de la columna de una hoja de Excel
#   teniendo en cuenta su nombre.
#   * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
#   * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
#
# Solución:
#   Se trata de un cambio de base, tomando como signos las letras 'A'..'Z'.
#
# Joaquín Ferrero, 20230810.
#
use v5.36;
use utf8;

##############################################################################
### Subrutinas
sub COLUMN($columna) {
    # Si devuelve 0 es que ha ocurrido un error
    # El rango de valores es [1..Inf)
    my $COLUMN = 0;

    # conversión de letra a número
    sub L2N($letra) { ord($letra) - ord('A') + 1 }

    # Normalización y filtrado de $columna para quedarnos sólo con las letras
    # (evitamos el caso de que nos pasen la referencia de una celda)
    $columna = uc $columna;
    $columna =~ s/[^A-Z]+//g;

    # Cálculo
    for my $letra (split //, $columna) {
        $COLUMN = $COLUMN * 26 + L2N($letra);
    }

    return $COLUMN;
}

##############################################################################
### Programa

my %pruebas = (
    A	      => 1,
    D	      => 4,
    AA	      => 27,
    ZZ	      => 702,
    E15784    => 5,
    CA        => 79,
    ''        => 0,
    cafe      => 53565,
    '$ABAD$4' => 18958,
    ABAD54    => 18958,
    ABAD      => 18958,
    MOUREDEV  => 109_305_094_128,
);

while (my($col, $val) = each %pruebas) {
    say "$col\t$val\t", COLUMN($col);
}

__END__
