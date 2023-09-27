#!/usr/bin/env perl
#
# Las sumas
#
# Crea una función que encuentre todas las combinaciones de los números
# de una lista que suman el valor objetivo.
# - La función recibirá una lista de números enteros positivos
#   y un valor objetivo.
# - Para obtener las combinaciones sólo se puede usar
#   una vez cada elemento de la lista (pero pueden existir
#   elementos repetidos en ella).
# - La salida es una lista con las combinaciones que suman el valor
#   objetivo. Si no hay combinaciones se devuelve una lista vacía.
#
# Ejemplo
#   Lista = [1, 5, 3, 2], Objetivo = 6
#   Solución: [1, 5] y [1, 3, 2]
#
use v5.38;
no warnings;
use utf8;
use feature 'refaliasing';             # A partir de Perl v5.22
no warnings 'experimental';
use List::Util 'sum';

prueba( [1, 5, 3, 2], 6 );
prueba( [1, 2, 3, 4, 5, 6, 7, 8, 9], 20 );

sub prueba ($array_ref, $objetivo) {
    say "Array: $array_ref->@*\nObjetivo: $objetivo";                  # A partir de Perl v5.24
    my @arrays_ref = busca_combinaciones_que_suman($array_ref, $objetivo);
    for \my @array (@arrays_ref) { say "[@array]" }                    # A partir de Perl v5.22
}

sub busca_combinaciones_que_suman ($array_ref, $objetivo, $array_parcial_ref = [], $encontrados = []) {
    while(my($i, $número) = each $array_ref->@*) {                     # A partir de Perl v5.12
        my $suma_temporal = $número + sum $array_parcial_ref->@*;      # Cuánto suma hasta ahora
        next if $suma_temporal > $objetivo;                            # Nos hemos pasado, probamos con otro $número
        my $array_parcial = [ $array_parcial_ref->@*, $número ];       # $array_parcial es lo que tenemos ahora, más el $número

        if ($suma_temporal == $objetivo) {                             # encontrada combinación
            push $encontrados->@*, $array_parcial;                     # agregamos $array_parcial como combinación encontrada
        }
        else {                                                         # aún no hemos llegado a $objetivo
            busca_combinaciones_que_suman(                             # buscamos otra combinación
                [ $array_ref->@[ $i+1 .. $array_ref->$#* ] ],          # con los números que siguen al actual
                $objetivo,                                             # buscamos este $objetivo
                $array_parcial,                                                # formada por esta combinación
                $encontrados
            );
        }
    }

    return $encontrados->@*;
}

