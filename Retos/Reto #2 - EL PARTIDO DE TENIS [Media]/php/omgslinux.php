<?php

const P1=0;
const P2=1;

function tennisresult($turnos): void
{
    $scores = ['Love', 15, 30, 40, 'Ventaja', 'Fin'];
    $players=['P1', 'P2'];

    $points = [
        P1 => 0,
        P2 => 0,
    ];
    $winner=null;
    $i=0;
    while(null==$winner && $i<count($turnos)) {
        $pX = $turnos[$i]; // Id del jugador, 0 o 1
        $points[$pX]++; // Puntos del jugador que gana el punto
        if ($points[$pX]>count($scores)) {
            $points[$pX]=count($scores)-1;
        }
        $sX = $points[$pX];
        $sY= $points[1-$pX]; // Puntos del otro jugador
        if (($sX>3) && (($sX - $sY) >1)) {
            // Gana el jugador X
            printf("Ha ganado el jugador %s\n", $players[$pX]);
            $winner=$players[$pX];
        } else {
            $scoreText = $scores[$points[0]] . ' - ' . $scores[$points[1]];
            if ($sX>2 && $sY>2) {
                if ($sY==$sX) {
                    // Hay que ganar por 2
                    $scoreText = 'Iguales';
                    if ($sX==3) {
                        $scoreText = 'Deuce';
                    }
                } else {
                    $scoreText = $scores[4] .' '.$players[$pX];
                }
            }
            printf("Tanto del jugador %s: %s\n",$players[$pX], $scoreText);
        }
        $i++;
    }
}

tennisresult([P1, P1, P1, P1, P1, P2, P1, P1]);
tennisresult([P1, P1, P2, P2, P1, P2, P1, P2, P1, P1]);
