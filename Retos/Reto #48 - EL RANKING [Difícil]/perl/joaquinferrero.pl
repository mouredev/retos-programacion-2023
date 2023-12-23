#!/usr/bin/env perl
#
# Listado calculado en tiempo real
#
# Crea un programa que muestre un listado calculado en tiempo real
# con todos los usuarios que han resuelto algún reto de programación
# de este año.
#
# - El listado debe estar ordenado por el número de ejercicios resueltos
#   por cada usuario (y mostrar ese contador al lado de su nombre).
# - También se debe de mostrar el número de usuarios que han participado
#   y el número de correcciones enviadas.
#
# Joaquín Ferrero, 20231219
#
use v5.10;
use Path::Tiny;

say "Lista de ejercicios resueltos por usuario";

my $iter = path(".")->iterator({recurse => 1});

my $total_correcciones;
while ($path = $iter->()) {
    # extraemos de la ruta el nombre del usuario
    next if $path !~ m[\]/\S+?/(?<name>.+?)[.].{1,6}$];
    next if $+{name} eq 'ejercicio';

    # Contamos una participación más de ese usuario
    $veces{$+{name}}++;

    # Contador de correcciones
    $total_correcciones++;
}

# De las claves, ordenamos por número de participaciones,
# y por orden alfabético en caso de empate
for (
    sort {
        $veces{$b} <=> $veces{$a}
        ||
        $a cmp $b
    }
    keys %veces
) {
    say "$veces{$_}\t$_";
}

# Totales
say "-" x 40;
say $total_correcciones, "\t", scalar keys %veces;

