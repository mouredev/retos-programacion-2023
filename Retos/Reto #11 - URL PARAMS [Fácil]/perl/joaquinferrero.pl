#!/usr/bin/env perl
#
# URL params
#
# Dada una URL con parámetros, crea una función que obtenga sus valores.
# No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#
# Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
# los parámetros serían ["2023", "0"]
#
# Joaquín Ferrero, 20230915
#
use v5.38;

my $URL = 'https://retosdeprogramacion.com?year=2023&challenge=0';

say for parametros($URL);


sub parametros($url) {
    $url =~ /=(.+?)(?:&|$)/g;
}

__END__

