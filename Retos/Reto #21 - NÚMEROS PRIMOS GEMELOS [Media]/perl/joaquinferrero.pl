#!/usr/bin/env perl
#
# Números primos gemelos
#
# Crea un programa que encuentre y muestre todos los pares de números primos
# gemelos en un rango concreto.
#
# El programa recibirá el rango máximo como número entero positivo.
#
# Un par de números primos se considera gemelo si la diferencia entre
# ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#
# Ejemplo: Rango 14
# (3, 5), (5, 7), (11, 13)
#
# Joaquín Ferrero, 20230919
#
use v5.38;
use builtin qw(true false);			# a partir de Perl v5.36
no warnings 'experimental::builtin';

sub es_primo($n) {
    for my $div (2 .. $n-1) {
        return false if $n % $div == 0;		# no es primo si es divisible
    }
    return true;
}

my $rango = shift;
my @resultado;

for my $i (5 .. $rango) {
    my $j = $i-2;

    push @resultado, "($j, $i)"  if es_primo($i) and es_primo($j);
}

say join ", ", @resultado;

