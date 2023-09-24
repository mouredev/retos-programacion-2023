#!/usr/bin/env perl
#
# Cuenta atrás
#
# Crea una función que reciba dos parámetros para crear una cuenta atrás.
# - El primero, representa el número en el que comienza la cuenta.
# - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
# - Sólo se aceptan números enteros positivos.
# - El programa finaliza al llegar a cero.
# - Debes imprimir cada número de la cuenta atrás.
#
# Joaquín Ferrero, 20230924
#
use v5.38;
use utf8;

print "Valor inicial: "; chomp(my $inicio = <>);
print "Segundos de espera: "; chomp(my $espera = <>);

$inicio = int 0+$inicio;
$espera = int 0+$espera;

die "ERROR: Los valores deben ser enteros positivos\n" unless $inicio > 0 and $espera > 0;

cuenta_atrás($inicio, $espera);


sub cuenta_atrás($inicio, $espera) {
    for (reverse 0 .. $inicio) {
        sleep $espera;
        say;
    }
}

