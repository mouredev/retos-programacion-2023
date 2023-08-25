#!/usr/bin/env perl
#
# Reto #14. «Octal y Hexadecimal»
#
# Programa:
#   Crea una función que reciba un número decimal y lo trasforme a Octal y Hexadecimal.
#   - No está permitido usar funciones propias del lenguaje de programación.
#
# Joaquín Ferrero, 20230817
#
use v5.36;
use utf8;
use open IO => ':locale';

while (1) {
    print "Introduzca un número a convertir a octal y hexadecimal (enter=fin): ";
    chomp(my $número = <>);
    last if 0 == length $número;

    my $octal = cambio_base($número, 8);
    my $hexa  = cambio_base($número,16);

    say "$número => 0$octal - 0x$hexa";
}

sub cambio_base($número, $base, $alfabeto = [0..9,"A".."Z"]) {
    # Rutina general que cambia un $número a una $base numérica usando
    # los símbolos indicados por $alfabeto
    #
    my $resultado = '';

    for (my $n = $número; $n > 0; ) {
        my $d = sprintf "%d", $n / $base;		# división entera redondeada
        my $r = $n - $d * $base;			# resto de la división entera
        $resultado = $alfabeto->[$r] . $resultado;	# acumulamos el dígito encontrado
        $n = $d;					# siguiente dígito
    }

    $resultado = $alfabeto->[0] if not $resultado;	# caso del '0'

    return $resultado;
}
