#!/usr/bin/env raku
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
use v6;

prueba( [1, 5, 3, 2], 6 );
prueba( [1, 2, 3, 4, 5, 6, 7, 8, 9], 20 );

sub prueba (@array, $objetivo) {
    say "Array: {@array}\nObjetivo: $objetivo";
    my @arrays = busca_combinaciones_que_suman(@array, $objetivo);
    for @arrays -> @array { "[{@array}]".say }
}

sub busca_combinaciones_que_suman (@array, $objetivo, @array_parcial = []) {
    my @encontrados = [];

    for @array.kv -> $i, $número {
        my $suma_temporal = @array_parcial.sum + $número;      	# Cuánto suma hasta ahora
        next if $suma_temporal > $objetivo;		       	# Nos hemos pasado, probamos con otro $número

        my @array_temporal = |@array_parcial, $número;	       	# @array_temporal es lo que tenemos ahora, más el $número

        if ($suma_temporal == $objetivo) {		       	# encontrada combinación
            push @encontrados, @array_temporal;		       	# agregamos @array_temporal como combinación encontrada
        }
        else {						       	# aún no hemos llegado a $objetivo
            push @encontrados,					# agregamos el resto de soluciones
                |busca_combinaciones_que_suman(		       	# buscamos otras combinaciones
                    [@array[ $i+1 .. * ]],			# con los números que siguen al actual
                    $objetivo,				       	# con este $objetivo
                    @array_temporal,			       	# formada por esta combinación inicial
                );
        }
    }

    return @encontrados;
}

