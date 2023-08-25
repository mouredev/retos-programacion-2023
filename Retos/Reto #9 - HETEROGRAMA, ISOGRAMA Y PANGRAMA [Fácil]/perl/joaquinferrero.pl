#!/usr/bin/env perl
#
# Reto #9. «Heterograma, isograma y pangrama»
#
# Programa:
#   * Crea 3 funciones, cada una encargada de detectar si una cadena de
#   * texto es un heterograma, un isograma o un pangrama.
#
#   * - heterograma: cada letra aparece una vez
#   * - isograma: cada letra aparece el mismo número de veces
#   * - pangrama: aparecen todas las letras del abecedario
#
# Joaquín Ferrero, 20230816
#
use v5.38;
use utf8;
use open OUT => ':locale';

use List::Util 'all';

my @ejemplos = (
    "yuxtaponer", "centrifugado", "luteranismo", "adulterinos", "hiperblanduzcos", "Centrifugadlos",

    "Whisky bueno: ¡excitad mi frágil pequeña vejez!",
    "Extraño pan de col y kiwi se quemó bajo fugaz vaho.",
    "Cada vez que trabajo Félix me paga con whisky añejo.",
    "Quiere la boca exhausta vid, kiwi, piña y fugaz jamón.", 
    "Jovencillo emponzoñado de whisky: ¡qué figurota exhibe!",
    "Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol.",
    "El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado un saxofón.",
    "El jefe buscó el éxtasis en un imprevisto baño de whisky y gozó como un duque.",
    "Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.",
    "José compró una vieja zampoña en Perú. Excusándose, Sofía tiró su whisky al desagüe de la banqueta.",
    "El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.",
    "El cadáver de Wamba, rey godo de España, fue exhumado y trasladado en una caja de zinc que pesó un kilo.",
    "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja.",
);

for my $ejemplo (@ejemplos) {
    print "[$ejemplo]\n\t";

    my %stats = estadísticas($ejemplo);

    my $es_heterograma = heterograma(%stats);
    my $es_isograma    = isograma(%stats);
    my $es_pangrama    = pangrama(%stats);

    print "Es heterograma. " if $es_heterograma;
    print "Es isograma. "    if $es_isograma;
    print "Es pangrama. "    if $es_pangrama;
    print "\n";
}

sub heterograma(%stats) {
    all { $_ == 1 } values %stats;
}

sub isograma(%stats) {
    my(undef, $val) = each %stats;	# primera clave,valor
    all { $_ == $val } values %stats;
}

sub pangrama(%stats) {
    my @ALFABETO = ('a'..'z','ñ');
    all { exists $stats{$_} } @ALFABETO;
}

sub estadísticas($texto) {
    my %conteo;
    $texto = lc $texto;			# normalizar a minúsculas
    $texto =~ tr/áéíóúü/aeiouu/;	# normalizar sin tildes

    for my $letra (split //, $texto) {
        next if $letra !~ /\w/;
        $conteo{$letra}++;
    }

    return %conteo;
}

