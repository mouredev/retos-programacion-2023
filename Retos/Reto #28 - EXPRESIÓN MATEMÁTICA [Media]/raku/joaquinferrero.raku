#!/usr/bin/env raku
#
# Expresión matemática
#
# Crea una función que reciba una expresión matemática (String)
# y compruebe si es correcta. Retornará true o false.
# - Para que una expresión matemática sea correcta debe poseer
#   un número, una operación y otro número separados por espacios.
#   Tantos números y operaciones como queramos.
# - Números positivos, negativos, enteros o decimales.
# - Operaciones soportadas: + - * / %
#
# Ejemplos:
#   "5 + 6 / 7 - 4" -> true
#   "5 a 6" -> false
#
# Joaquín Ferrero, 20230925
#
use v6;

my $expresión = prompt "Introduce la expresión matemática: ";

say "La expresión es { chequea-expresión-matemática($expresión) ?? "correcta." !! "incorrecta." }";


sub chequea-expresión-matemática($expresión) {
    grammar {
        token TOP       { ^ (<cifra> [ <.ws> <operador> <.ws> <cifra> ]+) <.ws> $ }
        token cifra     { <signo>? <entero> [ <[.]> <entero> ]? }
        token signo     { <[ + - ]> }
        token entero    { <[ 0 .. 9 ]>+ }
        token operador  { <[ * / % + - ]> }
    }.parse($expresión);

    return ?$/;
}

