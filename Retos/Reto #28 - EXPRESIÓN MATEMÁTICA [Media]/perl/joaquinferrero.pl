#!/usr/bin/env perl
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
use v5.38;
use builtin qw(true false);
use utf8;
use open qw':std :utf8';

print "Introduce la expresión matemática: "; chomp(my $expresión = <>);

print "La expresión es ", chequea_expresión_matemática($expresión) ? "correcta.\n" : "incorrecta.\n";


sub chequea_expresión_matemática($expresión) {
    return scalar(
        $expresión =~ qr/
            ^ (?&cifra) (?: \s+ (?&operador) \s+ (?&cifra))+ \s* $		# una o más cifras separadas por operadores
            (?(DEFINE)
                (?<cifra> (?&signo)? (?&entero) (?:[.] (?&entero))?)	# una cifra es un posible signo seguido de un entero y una parte decimal
                (?<signo> [+-])						# el signo que acompaña a la parte entera
                (?<entero> [0-9]+)						# la parte entera y decimal es un conjunto de dígitos
                (?<operador> [*\/%+-])					# operadores permitidos en la expresión
            )
        /x
    );
}

