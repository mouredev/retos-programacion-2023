#!/usr/bin/env perl
#
# Colores HEX y RGB
#
# Crea las funciones capaces de transformar colores HEX a RGB y viceversa.
#
# Ejemplos:
#   RGB a HEX: r: 0, g: 0, b: 0 -> #000000
#   HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
#
# Joaquín Ferrero, 20230919
#
use v5.38;

sub HEXtoRGB($HEX) { map { hex } $HEX =~ /([A-F\d]{2})/gi }
sub RGBtoHEX(@RGB) { '#' . join '', map { sprintf '%02X', $_ } @RGB }

say '(', join(',', HEXtoRGB('#32124D')), ')';
say '(',           RGBtoHEX(50, 18, 77), ')';

