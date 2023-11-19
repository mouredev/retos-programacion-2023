#!/usr/bin/env perl
#
# Terna pitagórica
#
# Crea una función que encuentre todos las ternas pitagóricas
# menores o iguales a un número dado.
#
# - Una terna pitagórica es un conjunto ordenado de tres números enteros positivos
#   a, b, c, y son solución de la ecuación diofántica cuadrática
#   a² + b² = c²
# - La función recibe el número máximo que puede aparecer en la terna.
#
# Ejemplo:
#   Las ternas menores o iguales a 10 son (3, 4, 5) y (6, 8, 10).
#
# Joaquín Ferrero, 20231005
#
use v5.38;
#use strict;					# activo desde Perl v5.12
#use warnings;					# activo desde Perl v5.35
use utf8;					# desde Perl v5.8
use open IO => qw(:utf8 :std);

my @ternas = ternas(100);

for my $terna (@ternas) {
    my($a, $b, $c) = $terna->@*;		# desde Perl v5.20

    say "($a, $b, $c):\t", $a**2, " + ", $b**2, " = ", $c**2;
}
say "Total ", scalar(@ternas), " ternas";


sub ternas($máximo) {				# desde Perl v5.36
    my @ternas;
    my %ternas_vistas;

    # Búsqueda exhaustiva, de todas las combinaciones
    for my $m ( 1 .. $máximo ) {
        for my $n ( $m .. $máximo ) {
            next if $ternas_vistas{"$m;$n"};	# sólo ternas únicas

            my $o = sqrt($m**2 + $n**2);

            next if $o > $máximo;		# fuera del límite
            next if int($o) != $o;		# no es terna

            # generación de ternas no primitivas
            for my $d (1 .. $máximo) {
                my $m2 = $d * $m;
                my $n2 = $d * $n;
                my $o2 = $d * $o;
                last if $o2 > $máximo or $m2 > $máximo or $n2 > $máximo;

                push @ternas, [ $m2, $n2, $o2 ];

                $ternas_vistas{"$m2;$n2"}++;
            }
        }
    }

    return @ternas;
}

__END__
@ternas = ternas_pitagóricas(100);
@ternas = ternas_pitagóricas_pitagóras(100);

sub ternas_pitagóricas_pitagóras($máximo) {
    my @ternas;

    # Método de Pitágoras
    # a = j²-1
    # b = 2j
    # c = j²+1
    # siendo j>0

    for my $j (1..$máximo) {
        my $a = $j**2 -1;
        my $b = 2*$j;
        my $c = $j**2 +1;
        last if $a > $máximo or $b > $máximo or $c > $máximo;

        push @ternas, [ $a, $b, $c ];
    }

    return @ternas;
}

sub ternas_pitagóricas($máximo) {
    my @ternas;

    # Método babilónico
    # a = m²-n²
    # b = 2mn
    # c = m²+n²,
    # siendo m>n

    # Doble bucle para los valores de m y n
    for my $n ( 1 .. $máximo-1 ) {
        for my $m ( $n+1 .. $máximo ) {
            my $a = $m**2 - $n**2;
            my $b = 2*$m*$n;
            my $c = $m**2 + $n**2;
            next if $a > $máximo  or  $b > $máximo  or  $c > $máximo;
            push @ternas, [ $a, $b, $c ];
        }
    }

    return @ternas;
}

