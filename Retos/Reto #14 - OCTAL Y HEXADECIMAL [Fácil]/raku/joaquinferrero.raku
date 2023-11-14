#!/usr/bin/env raku
#`(
    Reto #14. «Octal y Hexadecimal»
    
    Programa:
      Crea una función que reciba un número decimal y lo trasforme a Octal y Hexadecimal.
      - No está permitido usar funciones propias del lenguaje de programación.
    
    Joaquín Ferrero, 20230817
)
use v6.c;

loop {
    my $número = prompt "Introduzca un número a convertir a octal y hexadecimal (enter=fin): ";
    last if $número.chars == 0;

    my $octal = cambio_base($número, 8);
    my $hexa  = cambio_base($número,16);

    say "$número => 0$octal - 0x$hexa";
}

sub cambio_base($número, $base, @alfabeto = (|(0..9),|("A".."Z"))) {
    # Rutina general que cambia un $número a una $base numérica usando
    # los símbolos indicados por $alfabeto
    #
    my $resultado = '';

    loop (my $n = $número; $n > 0; ) {
        my $d = floor($n / $base);			# división entera redondeada
        my $r = $n - $d * $base;			# resto de la división entera
        $resultado = @alfabeto.[$r] ~ $resultado;	# acumulamos el dígito encontrado
        $n = $d;					# siguiente dígito
    }

    $resultado = @alfabeto.[0] if not $resultado;	# caso del '0'

    return $resultado;
}
