#!/usr/bin/env raku
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
use v6;
use Path::Finder;

say "Lista de ejercicios resueltos por usuario";

# Regla de los archivos que buscamos: nombre del directorio, y que han de ser archivos normales
my @archivos = Path::Finder.path(/ Reto \s . \d+ /).file.in("../../");

# De los archivos nos quedamos con su nombre, menos la extensión, y los metemos al saco
# menos los archivos "ejercicio"
my $saco = @archivos.map({ (.basename.split(/\./))[0] }).grep({ $_ ne "ejercicio" }).Bag;

# Del saco imprimimos los elementos ordenados por número de participaciones,
# y por orden alfabético en caso de empate
$saco.pairs.sort({ -$_.value, $_.key })».&{ say .value, "\t", .key };

# Totales
say "-" x 40;
say $saco.total, "\t", $saco.keys.elems;


=finish
#Otra forma:
my %veces;
@archivos.map: { %veces{ ($_.basename.split(/\./))[0] }++ };
%veces.keys.sort({ %veces{$^b} <=> %veces{$^a} || $^a cmp $^b })».&{ "%veces{$_}\t$_".say };
say @archivos.elems, "\t", %veces.keys.elems;
