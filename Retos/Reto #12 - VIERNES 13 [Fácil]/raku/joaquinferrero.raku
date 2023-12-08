#!/usr/bin/env raku
#`(
    Viernes 13

    Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
    - La función recibirá el mes y el año y retornará verdadero o falso.

    Joaquín Ferrero, 20230916
)
use v6;

my $fecha = prompt "Introduce mes y año: ";

my ($mes, $anno) = |($fecha ~~ /(\d+) \s+ (\d+)/);

say (hay_viernes_13($mes, $anno) ?? "Hay" !! "No hay"), " viernes 13";


sub hay_viernes_13($mes, $anno) {
    return Date.new($anno, $mes, 13).day-of-week == 5;
}

