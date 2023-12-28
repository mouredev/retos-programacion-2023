#!/usr/bin/env perl
#
# Permutaciones
#
# Crea un programa que sea capaz de generar e imprimir todas las
# permutaciones disponibles formadas por las letras de una palabra.
# - Las palabras generadas no tienen por qué existir.
# - Deben usarse todas las letras en cada permutación.
# - Ejemplo: sol, slo, ols, osl, los, lso
#
# Entrada
# Una texto (palabra)
#
# Joaquín Ferrero, 20230913
#
use v5.36;
use strict;
use warnings;

# Función para generar permutaciones recursivamente
sub permutaciones($prefijo, $string) {
    # $prefijo es la parte invariante de la cadena, al principio
    # $string es la parte que tenemos que permutar tras el $prefijo

    my $longitud = length $string;

    # Si no queda nada que permutar del resto, imprimimos el resultado y regresamos
    if ($longitud == 0) {
        say $prefijo;
    }
    else {
        for my $i (0 .. $longitud - 1) {
            # Formamos el $resto como lo anterior al carácter i-ésimo,
            # más lo que sigue tras ese mismo carácter
            my $resto = substr($string, 0, $i) . substr($string, $i + 1);

            # Permutamos el $prefijo más el carácter i-ésimo, junto con el $resto
            permutaciones($prefijo . substr($string, $i, 1), $resto);
        }
    }
}

# Solicitar una palabra al usuario
print "Ingresa una palabra: ";
my $palabra = <STDIN>;
chomp $palabra;

# Llamar a la función para generar permutaciones
say "Permutaciones de '$palabra':";
permutaciones("", $palabra);

__END__

