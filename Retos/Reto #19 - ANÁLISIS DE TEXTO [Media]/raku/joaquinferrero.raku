#!/usr/bin/env raku
#`(
    Análisis de texto
    
    Crea un programa que analice texto y obtenga:
    - Número total de palabras.
    - Longitud media de las palabras.
    - Número de oraciones del texto (cada vez que aparecen un punto).
    - Encuentre la palabra más larga.
    
    Todo esto utilizando un único bucle.
    
    Joaquín Ferrero, 20230918
)
use v6;

my $texto = q:to/END/;
    En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho 
    tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, 
    rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón 
    las más noches, duelos y quebrantos los sábados, lentejas los viernes, algún 
    palomino de añadidura los domingos, consumían las tres partes de su hacienda. 
    El resto della concluían sayo de velarte, calzas de velludo para las fiestas 
    con sus pantuflos de lo mismo, los días de entre semana se honraba con su 
    vellori de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta, y 
    una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así 
    ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo 
    con los cincuenta años, era de complexión recia, seco de carnes, enjuto de 
    rostro; gran madrugador y amigo de la caza. Quieren decir que tenía el 
    sobrenombre de Quijada o Quesada (que en esto hay alguna diferencia en los 
    autores que deste caso escriben), aunque por conjeturas verosímiles se deja 
    entender que se llama Quijana; pero esto importa poco a nuestro cuento; basta 
    que en la narración dél no se salga un punto de la verdad.
END

my @words = $texto.match(/\w+/, :global).flat;
my $words = @words.elems;

say "Total palabras: { $words }";
say "Longitud media: { @words.map({ .chars }).sum / $words }";
say "Núm. oraciones: { $texto.match(/\w<[.]>/, :global).elems }";
say "Palabra larga : { @words.map({ $_.chars => $_ }).max.value }";

=finish

# Solución desde Perl
my $total_palabras;
my $longitud_total;
my $oraciones;
my $máslarga_palabra;
my $máslarga_longitud = 0;

while $texto ~~ m:c/(\w+) (<[.]>)?/ {
    my $palabra = $0;
    $oraciones++ if defined $1;

    $total_palabras++;
    
    my $longitud = $palabra.chars;
    $longitud_total += $longitud;

    if  $máslarga_longitud < $longitud {
        $máslarga_longitud = $longitud;
        $máslarga_palabra  = $palabra;
    }
}

say "Total palabras: $total_palabras";
say "Longitud media: ", $longitud_total / $total_palabras;
say "Núm. oraciones: $oraciones";
say "Palabra larga : $máslarga_palabra";

