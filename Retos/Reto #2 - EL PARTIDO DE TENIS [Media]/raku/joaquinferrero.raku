#!/usr/bin/env raku
#`[
 Reto #2: EL PARTIDO DE TENIS
 Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

 Enunciado

 Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 gane cada punto del juego.

 - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
    15 - Love
    30 - Love
    30 - 15
    30 - 30
    40 - 30
    Deuce
    Ventaja P1
    Ha ganado el P1
 - Si quieres, puedes controlar errores en la entrada de datos.

 Joaquín Ferrero. 20230112
]

use v6;

my @puntuación_tenística = < Love 15 30 40 >;


sub MAIN(
  *@puntos where @puntos.elems > 3 && @puntos.all ~~ / P (1|2) /  #= puntos jugados: P[1|2] [ P[1|2] ... ] (mínimo 4 puntos)
) {
    # unificamos la entrada de todos los argumentos, tanto si recibimos un argumento o varios
    my $puntos_ganados = join(" ", @puntos);

    # ahora sí, extraemos los números de los jugadores y los pasamos a 0 o 1
    @puntos = $puntos_ganados ~~ m:g/ P <( 1 | 2 )> /;
    @puntos .= map: { $_ - 1 };

    # simular partido
    partido_de_tenis(@puntos);
}

sub partido_de_tenis (@puntos_en_juego) {
    my @puntuaciones = (0, 0);
    my Bool $fin_de_partido = False;

    while @puntos_en_juego  and  not $fin_de_partido {
        my $jugador_ganador = @puntos_en_juego.shift;
        my $el_otro_jugador = 1 - $jugador_ganador;
        my $resultado_del_punto = "";

        ++@puntuaciones[$jugador_ganador];          # el ganador suma un punto a sus puntuaciones

        # ajustar la puntuación si se llega a igualar en Ventaja
        if @puntuaciones.all > 3 {
            @puntuaciones .= map: { $_ - 1 };
        }

        # si la puntuación no llega a 4 puntos, informamos de manera normal
        if @puntuaciones.all <= 3 {
            $resultado_del_punto =
                "@puntuación_tenística[@puntuaciones[0]] - @puntuación_tenística[@puntuaciones[1]]";
        }

        # empate a 3 puntos, que llamamos "Deuce"
        if @puntuaciones.all == 3 {
            $resultado_del_punto = "Deuce";
        }

        # "Ventaja" si el jugador supera al rival a partir del cuarto punto
        if  @puntuaciones[$jugador_ganador] > 3
        and @puntuaciones[$jugador_ganador] > @puntuaciones[$el_otro_jugador] {
            $resultado_del_punto = "Ventaja P{1 + $jugador_ganador}";
        }

        # ver si es ganador: debe haber conseguido
        # * una puntuación de más de 4 puntos, y
        # * una diferencia de más de un punto con el adversario
        if  @puntuaciones[$jugador_ganador] > 3
        and @puntuaciones[$jugador_ganador] > 1 + @puntuaciones[$el_otro_jugador] {
            $resultado_del_punto = "Ha ganado el P{1 + $jugador_ganador}";
            $fin_de_partido = True;
        }

        say $resultado_del_punto;
    }

    # comprobar errores
    if @puntos_en_juego {
        note "ERROR: quedan puntos jugados después de alcanzar la victoria";
        exit 1;
    }

    if (not $fin_de_partido) {
        note "ERROR: no hay puntuaciones suficientes para saber el ganador";
        exit 1;
    }
}
