#!/usr/bin/env raku
#
# Tabla de multiplicar
#
# Crea un programa que sea capaz de solicitarte un número y se
# encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
# Debe visualizarse qué operación se realiza y su resultado.
#
# Ejemplo:
#   1 x 1 = 1
#   1 x 2 = 2
#   1 x 3 = 3
#   ...
#
# Joaquín Ferrero, 20231009
#
use v6;

my $número = prompt "Tabla de multiplicar del número: ";

(1..10).map({ "$número × $_ = {$número * $_}" })».say;

