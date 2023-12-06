#!/usr/bin/env perl
#
# Adivina la palabra
#
# Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos.
# - El juego comienza proponiendo una palabra aleatoria incompleta. Ejemplo: "m_ur_d_v", y el número de intentos.
# - La palabra debe ocultar de forma aleatoria letras y nunca puede comenzar ocultando más del 60 %.
# - Puedes utilizar las palabras que quieras y el número de intentos que consideres.
#
# - El usuario puede introducir únicamente una letra o una palabra de la misma longitud.
# - Si escribe una letra y acierta, se muestra esa letra en la palabra.
# - Si falla, se resta uno al número de intentos.
# - Si escribe una resolución y acierta, finaliza el juego.
# - En caso contrario, se resta uno al número de intentos.
# - Si el contador de intentos llega a 0, el jugador pierde.
#
# Joaquín Ferrero, 20230914
#
use v5.24;
use utf8;
use open IO => ':locale';
use Path::Tiny;
use List::Util 'uniq';

# Selección de la palabra al azar
my $vocabulario = path("/usr/share/dict/spanish");
my @palabras = map { chomp; $_ } grep { length($_) >= 4 and length($_) <= 20 } $vocabulario->lines_utf8;
my $palabra = $palabras[rand @palabras];
my $largo_palabra = length $palabra;

# Ocultando letras
my $palabra_oculta = $palabra;
my $numero_sustituciones;
do {
    my @letras =  uniq grep { $_ ne "_" } split "", $palabra_oculta;
    my $letra_a_cambiar = $letras[int rand @letras];
    $palabra_oculta =~ s/$letra_a_cambiar/_/g;
    $numero_sustituciones = $palabra_oculta =~ tr/_/_/;
} while ($numero_sustituciones / $largo_palabra < 0.6);

say $palabra_oculta;

# Juego
my $intentos = 10;

my $prueba;
do {
    print "Quedan $intentos intentos. Introduzca letra o palabra: "; chomp($prueba = <STDIN>);

    if (length($prueba) == 1) {
        my $palabra_oculta_anterior = $palabra_oculta;
        
        # Reponemos la letra a la palabra oculta
        while ($palabra =~ m/$prueba/g) {		# buscar la $prueba en la $palabra
            # Colocamos la $prueba en la misma posición de la $palabra_oculta
            substr($palabra_oculta, pos($palabra)-1, 1) = $prueba;
        }
        
        say $palabra_oculta;				# mostramos cambios

        if ($palabra_oculta_anterior ne $palabra_oculta) {
            $intentos++;				# reponemos intento en caso de acertar
        }

        $prueba = $palabra_oculta;			# para ver si hemos terminado ya
    }

} while ($prueba ne $palabra  and  --$intentos);

# Resultado
if ($intentos > 0) {
    say "¡Resuelto!";
}
else {
    say "Lo siento, la palabra era '$palabra'";
}

