#!/usr/bin/perl
#
# Reto #4: PRIMO, FIBONACCI Y PAR
#### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23
#
## Enunciado
#
# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#
# Joaquín Ferrero. 20230127
#
use v5.36;
use utf8;
use open 'locale';

use builtin qw(true false);
use feature qw'switch signatures';
no warnings 'experimental';

### Subrutinas ##########################################
sub esPar($número) {
    $número % 2 == 0;
}

sub esPrimo($número) {
    given ($número) {
        when ($_  < 2)    { return false }
        when ($_ == 2)    { return true  }
        when (esPar($_))  { return false }
        default {
            for my $i ( 3 .. sqrt $número ) {
                return false  if  $número % $i  ==  0;
            }
        }
    }

    return true;
}

sub esFibonnaci($número) {
    my ($anterior, $actual) = (-1,1);

    while ($actual < $número) {
        ($anterior,$actual) = ($actual,$anterior+$actual);
    }

    return $número == $actual;
}


### Pedir información ###################################
my $número;

if (@ARGV) {
    $número = shift;
}
else {
    print "Introduce un número a analizar: ";
    $número = <<>>;
}

$número = int(0+ $número);				# nos aseguramos de que es un número entero
die "ERROR: el número debe ser positivo.\n" if $número < 0;


### Análisis ############################################
my $esPar = esPar($número);
my $esPrimo = esPrimo($número);
my $esFibonacci = esFibonnaci($número);


### Salida ##############################################
say $número, ($esPrimo ? " ":" no "), "es primo,", ($esFibonacci ? " ":" no "), "es fibonacci y es ", ($esPar ? "par":"impar");


__END__
