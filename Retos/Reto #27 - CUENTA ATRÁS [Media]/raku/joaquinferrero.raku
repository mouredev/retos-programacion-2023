#!/usr/bin/env raku
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
use v6;

sub MAIN(
    Int $inicio where * > 0,			#= Valor inicial
    Int $espera where * > 0			#= Segundos de espera
) {
    for reverse 0 .. $inicio {
        sleep $espera;
        .say;
    }
}

