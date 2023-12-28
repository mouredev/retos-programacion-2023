#!/usr/bin/perl
#
# Reto #2: EL PARTIDO DE TENIS
#### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23
#
## Enunciado
#
# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# gane cada punto del juego.
#
# - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#   15 - Love
#   30 - Love
#   30 - 15
#   30 - 30
#   40 - 30
#   Deuce
#   Ventaja P1
#   Ha ganado el P1
# - Si quieres, puedes controlar errores en la entrada de datos.
# - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
#
# Joaquín Ferrero. 20230110
#
use v5.28;
use utf8;
use open ':locale';

# Argumentos
@ARGV or die "Uso: $0 <lista de resultados de los partidos: P1 P2 ...>\n";

my $ganados = join "," => @ARGV;                    # unimos todos los argumentos en uno solo
my @ganados = $ganados =~ /P(1|2)/g;                # extraemos los números de los jugadores

@ganados > 3 or die "ERROR: la secuencia es demasiado corta\n";

# la extraña puntuación de los tenistas
my @puntuación_tenística = qw( Love 15 30 40 );

# Simulación de partido
my @puntos = (0, 0, 0);                             # puntos obtenidos por cada jugador
my $fin_de_partido = "";

while (@ganados  and  not $fin_de_partido) {        # para todos los puntos
    my $jugador = shift @ganados;                   # ver qué jugador ha ganado
    my $otro_jugador = 3 - $jugador;                # el otro jugador (1 o 2)
    my $resultado = "";                             # texto resultado, por líneas

    #print "P$jugador : ";

    ++$puntos[$jugador];                            # le sumamos un punto y vemos las puntuaciones
    
    # ajustar la puntuación si se llega a igualar en Ventaja
    if ($puntos[$jugador] > 3  and  $puntos[$otro_jugador] > 3) {
        @puntos[1,2] = map { $_-1 } @puntos[1,2];
    }

    #print +(join "-" => @puntos[1,2]), " : ";

    # si la puntuación no llega a 40, informamos de manera normal
    if ($puntos[1] <= 3  and  $puntos[2] <= 3) {
        $resultado = "$puntuación_tenística[$puntos[1]] - $puntuación_tenística[$puntos[2]]";
    }

    # empate a 40, que llamamos "Deuce"
    if ($puntos[$jugador] == 3  and  $puntos[$otro_jugador] == 3) {
        $resultado = "Deuce";
    }

    # "Ventaja" si superamos al rival
    if ($puntos[$jugador] > 3  and  $puntos[$jugador] > $puntos[$otro_jugador]) {
        $resultado = "Ventaja P$jugador";
    }

    # ver si es ganador: debe haber conseguido
    # * una puntuación de más de 40 puntos, y
    # * una diferencia de un punto superior al del adversario
    if ($puntos[$jugador] > 3  and  $puntos[$jugador] > 1 + $puntos[$otro_jugador]) {
        $resultado = "Ha ganado el P$jugador";
        $fin_de_partido = "si";
    }

    say $resultado;
}

# comprobar si quedan puntos
if (@ganados) {
    die "ERROR: quedan puntos jugados después de alcanzar la victoria\n";
}

if (not $fin_de_partido) {
    die "ERROR: no hay puntuaciones suficientes para saber el ganador\n";
}

