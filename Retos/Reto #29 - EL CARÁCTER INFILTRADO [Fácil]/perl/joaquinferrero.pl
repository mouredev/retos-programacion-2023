#!/usr/bin/env perl
#
# El carácter infiltrado
#
# Crea una función que reciba dos cadenas de texto casi iguales,
# a excepción de uno o varios caracteres.
# La función debe encontrarlos y retornarlos en formato lista/array.
# - Ambas cadenas de texto deben ser iguales en longitud.
# - Las cadenas de texto son iguales elemento a elemento.
# - No se pueden utilizar operaciones propias del lenguaje
#   que lo resuelvan directamente.
#
# Ejemplos:
# - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
# - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
#
# Joaquín Ferrero, 20230925
#
use v5.38;
use utf8;
use open qw<:std :utf8>;


busca_diferencias("Cadenas de distinta longitud", "Otra cadena");

my @diferencias;

@diferencias = busca_diferencias("Una cadena igual", "Una cadena igual");
pinta_diferencias(@diferencias);

@diferencias = busca_diferencias("Me llamo mouredev", "Me llemo mouredov");
pinta_diferencias(@diferencias);

@diferencias = busca_diferencias("Me llamo.Brais Moure", "Me llamo brais moure");
pinta_diferencias(@diferencias);

@diferencias = busca_diferencias("Me llamo Brais Moure", "Me llamó Bráis Mouré");
pinta_diferencias(@diferencias);


sub pinta_diferencias(@diferencias) {
    say "[", join(", ", map { qq{"$_"} } @diferencias), "]";
}

sub busca_diferencias($cadena_1, $cadena_2) {
    if (length($cadena_1) != length($cadena_2)) {
        warn "ERROR: Las cadenas\n  [$cadena_1] y\n  [$cadena_2]\n    tienen distinta longitud\n";
        return;
    }

    # ^. es el OR exclusivo para cadenas, a partir de Perl v5.28
    # A partir de aquí, serán "\0" los caracteres que coincidan entre las dos cadenas
    my @mezcla = split //, $cadena_1 ^. $cadena_2;

    # Recorrer la $mezcla para ver qué caracteres de $cadena_2 han cambiado
    my @diferentes;

    while(my($i, $letra) = each @mezcla) {		# A partir de Perl v5.12
        next if $letra eq "\0";
        push @diferentes, substr $cadena_2, $i, 1;
    }

    return @diferentes;
}

