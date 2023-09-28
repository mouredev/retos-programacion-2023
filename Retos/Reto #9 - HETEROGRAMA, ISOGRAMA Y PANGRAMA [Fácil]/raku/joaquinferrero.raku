#!/usr/bin/env raku
#`(
    Reto #9. «Heterograma, isograma y pangrama»

    Programa:
      * Crea 3 funciones, cada una encargada de detectar si una cadena de
      * texto es un heterograma, un isograma o un pangrama.

      * - heterograma: cada letra aparece una vez
      * - isograma: cada letra aparece el mismo número de veces
      * - pangrama: aparecen todas las letras del abecedario

    Joaquín Ferrero, 20230816
)
use v6.c;

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

for @ejemplos -> $ejemplo {
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
    %stats.values.all == 1;			# probar si todos los valores son igual a 1
}

sub isograma(%stats) {
    my ($val, @resto) = %stats.values;		# uno de los valores del hash
    @resto.all == $val;				# probar si son todos iguales al primero
}

sub pangrama(%stats) {
    %stats{ |('a'..'z'), 'ñ' }:exists.all.so == True;
}

sub estadísticas($texto) {
    my %conteo;
    my $texto-normal;

    $texto-normal =  lc $texto;			# normalizar a minúsculas
    $texto-normal ~~ tr/áéíóúü/aeiouu/;		# normalizar sin tildes

    for $texto-normal.comb {
        %conteo{$_}++ if /\w/;
    }

    return %conteo;
}

