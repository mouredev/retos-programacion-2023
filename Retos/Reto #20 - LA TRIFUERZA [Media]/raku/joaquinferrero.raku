#!/usr/bin/env raku
#`(
    La Trifuerza
    
    Crea un programa que dibuje una Trifuerza de "Zelda"
    formada por asteriscos.
    - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
    - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
    
    Ejemplo: Trifuerza 2
    
       *
      ***
     *   *
    *** ***
    
    Joaquín Ferrero, 20230919
) 
use v6;

sub MAIN(
    Int $trifuerza where * > 1		#= Tamaño Trifuerza (>1)
) {
    for 1, 2 -> $triángulo {
        for 0 .. $trifuerza-1 -> $i {
            say (' ' xx ($trifuerza*(3 - $triángulo) - $i - 1)).join,	# margen izquierdo
                join(							# los triángulos se forman
                    (' ' xx ($trifuerza*2 - $i*2 - 1)).join,		# unidos por espacios en blanco
                    ('*' xx ($i*2 + 1)).join				# tantos tramos de '*'
                         xx $triángulo					# tantos como triángulos haya que pintar
                );
        }
    }
}

