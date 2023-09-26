#!/usr/bin/env perl
#
# Cifrado César
#
# Crea un programa que realize el cifrado César de un texto y lo imprima.
# También debe ser capaz de descifrarlo cuando así se lo indiquemos.
#
# Te recomiendo que busques información para conocer en profundidad cómo
# realizar el cifrado. Esto también forma parte del reto.
#
# Joaquín Ferrero, 20230924
#
use v5.38;
use builtin qw(true false);		# a partir de Perl v5.36
no warnings 'experimental';
use utf8;
use open IO => ':locale';


sub cifra_césar($texto, $cifrar = true, $desplazamiento = 3) {
    my @alfabeto = qw( a á b c ç d e é f g h i í j k l m n ñ o ó p q r s t u ú ü v w x y z );
    my %alfabeto = map { $alfabeto[$_] => $_ } keys @alfabeto;
    $desplazamiento = -$desplazamiento if $cifrar;
    my $texto_cifrado;

    for my $letra (split //, $texto) {
        my $letra_en_minúscula = lc $letra;
        my $letra_es_mayúscula = true if $letra eq uc $letra;

        if (exists $alfabeto{$letra_en_minúscula}) {
            my $letra_cifrada =  $alfabeto[ ($alfabeto{$letra_en_minúscula} + $desplazamiento) % @alfabeto ];
            $letra_cifrada = uc($letra_cifrada) if $letra_es_mayúscula;

            $texto_cifrado .=  $letra_cifrada;
        }
        else {
            $texto_cifrado .= $letra;
        }
    }

    return $texto_cifrado;
}

sub    cifra($texto, $desplazamiento = 3) { cifra_césar $texto, true,  $desplazamiento }
sub descifra($texto, $desplazamiento = 3) { cifra_césar $texto, false, $desplazamiento }

say    cifra("Mi nombre es MoureDev. ¿Seguro?");
say descifra("Jf kmjzóc cp JmrócBcu. ¿Pceróm?");

