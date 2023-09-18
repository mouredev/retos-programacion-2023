#!/usr/bin/env perl
#
# Viernes 13
#
# Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
# - La función recibirá el mes y el año y retornará verdadero o falso.
#
# Joaquín Ferrero, 20230916
#
use v5.38;
use utf8;
use open IO => ':locale';
use Time::Local qw( timelocal_modern );

print "Introduce mes y año: "; chomp(my $fecha = <>);

my($mes, $anno) = $fecha =~ /(\d+)\s+(\d+)/ or die "Error en la introducción de datos\n";

say +(hay_viernes_13($mes, $anno) ? "Hay" : "No hay"), " viernes 13";


sub hay_viernes_13($mes, $anno) {
    # 6 es el índice que representa al día de la semana, en el array devuelto por localtime.
    # 5 representa al viernes, dentro de los valores devueltos en la posición 6.
    # Calculamos el epoch del día 1 de ese mes, y le sumamos 12 días, para ver si es viernes.
    return 5 == (localtime(timelocal_modern( 0, 0, 0, 1, $mes-1, $anno) +12*86400))[6];
}

__END__

