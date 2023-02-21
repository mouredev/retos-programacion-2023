#!/usr/bin/env perl
#
# «Piedra, papel, tijera, Spock, lagarto»
#
#    Juego original de Sam Kass y Karen Bryla, de principios de los años 90 del siglo XX.
#    http://www.samkass.com/theories/RPSSL.html
#
#    Se trata de una variante del juego de manos «Piedra, papel, tijera»
#    con armas adicionales: https://en.wikipedia.org/wiki/Rock_paper_scissors#Additional_weapons
#
#    Popularizado por la serie de televisión norteamericana «The Big Bang Theory»
#    https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock
#
#    mencionado en los episodios
#
#    + 02x08 - The Lizard-Spock Expansion, https://bigbangtheory.fandom.com/wiki/The_Lizard-Spock_Expansion
#      donde se explican las reglas del juego
#
#    + 05x17 - The Rothman Disintegration, https://bigbangtheory.fandom.com/wiki/The_Rothman_Disintegration
#      donde se reconoce al autor del juego (todos gritan ¡Hail, Sam Kass!)
#
#
# Programa:
#
#   Este programa muestra el ganador o empate entre dos jugadores después de
#   una serie de jugadas.
#   Las jugadas se indican con pares de las armas mostradas por los jugadores.
#   Las armas posibles son:
#     - "✊" o "D" (piedra)
#     - "✋" o "P" (papel)
#     - "✌" o "T" (tijera)
#     - "🖖" o "S" (spock)
#     - "🦎" o "L" (lagarto)
#
#   En esta versión del programa, la jugada se indica como una lista de
#   listas: ( [ , ], [ , ], [ , ] )
#
#   El resultado puede ser: "Jugador 1", "Jugador 2" o "Empate".
#
#   No hay control de errores a la entrada.
#
#
# Solución:
#
#     La forma de solucionar el problema consiste en agrupar y consultar las
#   armas en una estructura circular: si colocamos las armas en el orden
#   clásico: piedra, papel, tijeras, Spock, lagarto, entonces cada arma vence
#   al arma anterior (diferencia -1) y a la que está en dos posiciones más
#   adelante (+2), y a su vez es vencida por las otras dos (-2 y +1). En caso
#   de coincidencia (0), se trata como empate.
#
#     Entonces, se traducen las armas jugadas a su valor numérico posicional,
#   se calcula la distancia (diferencia) entre ellas, y se consulta un array
#   donde se guarda el resultado de la jugada (-1, 0, 1 siempre con respecto
#   al jugador 1), y se actualizan contadores según ese resultado.
#
#     Al final, se muestra el resultado en pantalla (el jugador que más
#   victorias tiene o empate).
#
#
# Ejemplo:
#
#   Lagarto (4) <-> Piedra (0)
#
#   la diferencia (valor de la jugada del jugador 2: 0 - valor de la jugada
#   jugador 1: 4) es -4. Ajustada a la lista circular se convierte en 1
#   (o sea, la piedra sigue al lagarto). El valor de la jugada entonces
#   es el valor del elemento 1 en el array de valoración: -1. Por lo tanto,
#   en la jugada anterior, el jugador 1 pierde.
#
#   En efecto, la piedra aplasta al lagarto.
#
#
# Joaquín Ferrero, 20230211.
#
use v5.36;
use experimental 'declared_refs';
use utf8;					# hay caracteres UTF8 en el código


##############################################################################
### Constantes

my %arma = (					# armas, con su posición numérica
    "D" => 0,   # pieDra
    "P" => 1,	# Papel
    "T" => 2,	# Tijeras
    "S" => 3,	# Spock
    "L" => 4,	# Lagarto

    "✊" => 0,	# piedra 
    "✋" => 1,   # papel  
    "✌" => 2,   # tijeras
    "🖖" => 3,   # spock  
    "🦎" => 4,   # lagarto
);

my @valores = ( 0, -1, +1, -1, +1 );		# resultados de ganancias y perdidas


##############################################################################
### Programa

juego( ["✋", "✊",], ["✌", "🖖",], ["✊", "🦎"] );				# Jugador 1

juego( ["✋", "✋" ], ["✊","✋"], ["🖖","✌"], ["🦎","✊"] );			# Jugador 2

juego( ["S", "L"], ["S", "D"], ["S", "P"], ["S", "T"], ["D","D"] );	# Empate


##############################################################################
### Subrutinas

sub juego(@jugadas) {

    # Puntuaciones de este juego:
    # [0] contador de empates
    # [1] contador de jugadas ganadas por jugador 1
    # [2] contador de jugadas ganadas por jugador 2
    # (en realidad, accedemos al índice [2] con el índice [-1]
    #
    my @puntuaciones = (0) x 3;

    for my \@jugada ( @jugadas ) {				# para todas las jugadas
        my($jugada1, $jugada2) =				# transformamos iconos a su valor numérico
            ($arma{$jugada[0]}, $arma{$jugada[1]});

        my $diferencia = $jugada2 - $jugada1;			# diferencia de valor
        $diferencia += 5 if $diferencia < 0;			# si es negativa, lo pasamos a positiva
        							# para que esté en el rango [0,4]
        
        my $resultado = $valores[$diferencia];			# 0: empate, 1: ganó jugador 1, -1: ganó jugador 2
        
        $puntuaciones[$resultado]++;				# anotamos un punto más
    }

    if ($puntuaciones[1] > $puntuaciones[2]) {			# según la puntuación obtenida
        say "Jugador 1";					# mostramos quién ganó
    }
    elsif ($puntuaciones[1] < $puntuaciones[2]) {
        say "Jugador 2";
    }
    else {							# o se empató
        say "Empate";
    }
}
