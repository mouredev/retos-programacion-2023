#!/usr/bin/env raku
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
use v6;

sub cifra-césar($texto, $hay-que-cifrar = True, $desplazamiento = 3) {
    my @alfabeto = <a á b c ç d e é f g h i í j k l m n ñ o ó p q r s t u ú ü v w x y z>;
    my %índice-a-letra = @alfabeto.kv;
    my %letra-a-índice = %índice-a-letra.invert;

    my $shift = $desplazamiento;		# separación entre alfabetos normal y codificado
    $shift *= -1 if $hay-que-cifrar;		# al decodificar se invierte el sentido del desplazamiento

    my $texto-cifrado = [~] gather {		# resultado de la (des)codificación
        for $texto.comb -> $letra {
            my $letra-índice = %letra-a-índice{$letra};
            my Bool $letra-es-mayúscula = not defined $letra-índice;
            my $letra-en-minúscula = $letra-es-mayúscula
                ?? do {
                    my $l = $letra.lc;
                    $letra-índice = %letra-a-índice{$l};
                    $letra-es-mayúscula = False if not defined $letra-índice;   # Es un carácter no alfabético
                    $l;
                }
                !!  $letra;

            take do {
                my $letra-cifrada = (defined $letra-índice)
                    ?? %índice-a-letra{($letra-índice + $shift) % @alfabeto}
                    !! $letra;

                $letra-cifrada = $letra-cifrada.uc if $letra-es-mayúscula;
                $letra-cifrada;
            };
        }
    }

    return $texto-cifrado;
}

sub    cifra($texto, $desplazamiento = 3) { cifra-césar $texto, True,  $desplazamiento }
sub descifra($texto, $desplazamiento = 3) { cifra-césar $texto, False, $desplazamiento }

say    cifra("Mi nombre es MoureDev. ¿Seguro?");
say descifra("Jf kmjzóc cp JmrócBcu. ¿Pceróm?");

