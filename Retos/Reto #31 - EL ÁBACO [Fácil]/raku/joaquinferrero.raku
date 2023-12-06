#!/usr/bin/env raku
#
# «El Ábaco»
#
# Programa:
#
#   Crear una función que sea capaz de leer el número representado por el ábaco.
#   * El ábaco se representa por un array con 7 elementos.
#   * Cada elemento tendrá 9 "O" para las cuentas y una secuencia de "---" para el alambre.
#   * El primer elemento del array representa los millones y el último las unidades.
#   * El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
#
# Solución:
#
#       El paso del ábaco será en forma de una referencia a un array de strings.
#
#       Recorrer todos los alambres, convertir las cuentas a dígitos y agregarlos
#   en una cifra. Formatear la cifra con delimitadores de millares e imprimirla en pantalla.
#
# Joaquín Ferrero, 20230807.
#
use v6.c;

##############################################################################
### Subrutinas
sub ábaco(@ábaco) {

    # Nuestra $cifra será la unión (join) de una recolección (gather)
    my $cifra = gather {
        for @ábaco -> $alambre {
            # Buscamos en el $alambre, desde el principio (^) al final ($),
            # con captura de las "O" iniciales (O*), seguidas por 3 guiones (\- ** 3),
            # y posiblemente algo más (.*).
            #
            $alambre ~~ m/^ (O*) \- ** 3 .* $/;

            # Si encontramos el patrón (y así debe ser si el $alambre está bien),
            # recolectamos el número de caracteres de la cadena capturada.
            #
            take $0.chars;
        }
    }.join;

#    OTRA FORMA, usando una substitución no destructiva
#    my $cifra = @ábaco.map({ S[^ (O*) \- ** 3..3 .* $] = $0.chars }).join;


    # quitamos los ceros a la izquierda
    $cifra = 0+ $cifra;

    # Formateo de la cifra con los delimitadores de millares
    # Tomamos el número de alambres, y lo recorremos de final a principio, cada
    # 3 dígitos, e insertamos un delimitador ".".
    #
    loop (my $pos = -3; $pos > -$cifra.chars; $pos -= 3) {
        $cifra.substr-rw(*+$pos, 0) = '.';
        $pos--;
    }

    return $cifra;
}

##############################################################################
### Programa

# 1.302.790
say ábaco([<
    O---OOOOOOOO
    OOO---OOOOOO
    ---OOOOOOOOO
    OO---OOOOOOO
    OOOOOOO---OO
    OOOOOOOOO---
    ---OOOOOOOOO
>]);

# 9.876.543.210
say ábaco([<
    OOOOOOOOO---
    OOOOOOOO---O
    OOOOOOO---OO
    OOOOOO---OOO
    OOOOO---OOOO
    OOOO---OOOOO
    OOO---OOOOOO
    OO---OOOOOOO
    O---OOOOOOOO
    ---OOOOOOOOO
>]);

# 0
say ábaco([<
    ---OOOOOOOOO
    ---OOOOOOOOO
    ---OOOOOOOOO
    ---OOOOOOOOO
    ---OOOOOOOOO
    ---OOOOOOOOO
    ---OOOOOOOOO
>]);

