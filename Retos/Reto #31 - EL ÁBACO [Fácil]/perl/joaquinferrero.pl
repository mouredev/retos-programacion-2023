#!/usr/bin/env perl
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
use v5.36;
use utf8;

##############################################################################
### Subrutinas
sub ábaco($ábaco_ref) {

    my $cifra;

    for ($ábaco_ref->@*) {
        # Hacemos una sustitución de toda la cadena, desde el principio (^) al
        # final ($), de la longitud (length) del primer ($1) par de paréntesis de
        # captura con los posibles "O" (O*).
        # Los modificadores que usamos son:
        # · /e para indicar ejecución de código Perl en la parte de sustitución, y
        # · /r para obtener del operador s/// el resultado de la sustitución,
        #      no el número de sustituciones.
        #
        $cifra .= s/^(O*).*$/length $1/re;
    }

    # quitamos los ceros a la izquierda
    $cifra = 0+ $cifra;

    # Formateo de la cifra con los delimitadores de millares
    # Tomamos el número de alambres, y lo recorremos de final a principio, cada
    # 3 dígitos, e insertamos un delimitador ".".
    #

    for (my $pos = -3; $pos > -length $cifra; $pos -= 3) {
        substr($cifra, $pos, 0) = '.';
        $pos--;
    }

    return $cifra;
}

##############################################################################
### Programa

# 1.302.790
say ábaco([qw(
    O---OOOOOOOO
    OOO---OOOOOO
    ---OOOOOOOOO
    OO---OOOOOOO
    OOOOOOO---OO
    OOOOOOOOO---
    ---OOOOOOOOO
)]);

# 9.876.543.210
say ábaco([qw(
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
)]);

# 0
say ábaco([qw(
    ---OOOOOOOOO
    ---OOOOOOOOO
    ---OOOOOOOOO
    ---OOOOOOOOO
    ---OOOOOOOOO
    ---OOOOOOOOO
    ---OOOOOOOOO
)]);

__END__
