#!/usr/bin/env perl
#
# Reto #16. «La escalera»
#
# Programa:
#   Crea una función que dibuje una escalera según su número de escalones.
#
#   - Si el número es positivo, será ascendente de izquierda a derecha.
#   - Si el número es negativo, será descendente de izquierda a derecha.
#   - Si el número es cero, se dibujarán dos guiones bajos (__).
#
# Joaquín Ferrero, 20230823
#
use v5.38;

say "[4]";  escalera( 4);
say "[-5]"; escalera(-5);
say "[0]";  escalera( 0);

sub escalera($escalones) {
    # Si $escalones es 0, el bucle se ejecuta una vez.
    # Si es mayor que cero o menor que cero, hay una fórmula matemática para
    # calcular los espacios que están delante de los escalones.
    my $s = $escalones <=> 0;			# signo: -1,0,1
    my @escalones = ('__','_|','|_');		# formas de los escalones, indexadas por $s; [-1] es el último
    my $e = 0;
    do {
        say "  " x (($escalones + abs $escalones)/2 - $e * $s - ($s > 0)), $escalones[$s];
    } while (++$e < abs($escalones) );
}
