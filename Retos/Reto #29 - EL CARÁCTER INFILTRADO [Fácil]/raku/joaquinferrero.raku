#!/usr/bin/env raku
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
use v6;


busca-diferencias("Cadenas de distinta longitud", "Otra cadena");

my @diferencias;

@diferencias = busca-diferencias("Una cadena igual", "Una cadena igual");
pinta-diferencias(@diferencias);

@diferencias = busca-diferencias("Me llamo mouredev", "Me llemo mouredov");
pinta-diferencias(@diferencias);

@diferencias = busca-diferencias("Me llamo.Brais Moure", "Me llamo brais moure");
pinta-diferencias(@diferencias);

@diferencias = busca-diferencias("Me llamo Brais Moure", "Me llamó Bráis Mouré");
pinta-diferencias(@diferencias);


sub pinta-diferencias(@diferencias) {
    "[%s]\n".printf: @diferencias.map({qq/"$_"/}).join(", ");
}

sub busca-diferencias($cadena_1, $cadena_2) {
    if $cadena_1.chars != $cadena_2.chars {
        note "ERROR: Las cadenas\n  [$cadena_1] y\n  [$cadena_2]\n    tienen distinta longitud\n";
        return;
    }

    # ~^ es el OR exclusivo para cadenas
    # A partir de aquí, serán "\0" los caracteres que coincidan entre las dos cadenas
    my @mezcla = ($cadena_1 ~^ $cadena_2).comb;

    # Recorrer la $mezcla para ver qué caracteres de $cadena_2 han cambiado
    my @diferentes;

    for @mezcla.kv -> $i, $letra {
        next if $letra eq "\0";
        @diferentes.push: substr $cadena_2, $i, 1;
    }

    return @diferentes;
}

