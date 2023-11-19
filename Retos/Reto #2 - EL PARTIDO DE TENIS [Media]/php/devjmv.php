<?php

$secuencia = ['P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'];
//suponiendo que la entrada de la secuencia este validada y corecta.

//jugador 1
$puno = 0;
//jugador 2
$pdos = 0;
foreach ($secuencia as $key => $jugada) {
    $puntuacion = '';
    //sumo los puntos segun el jugador
    $jugada == 'P1' ? $puno += 15 : ($jugada == 'P2' ? $pdos += 15 : null);
    //compruebo que sean iguales solo en 45 puntos o mayor
    if ($puno >= 45 && $puno == $pdos){
        $puntuacion = 'Deuce';
        echo $puntuacion. ' </br>';
        continue;
    }
    //compruebo al ganador
    if (($puno - $pdos >= 30 || $pdos - $puno >= 30) && ($puno > 45 || $pdos > 45)) {
        $puntuacion = 'Ha ganado el ' .$jugada;
        echo $puntuacion. ' </br>';
        break;
    }
    //compruebo la ventaja del jugador
    if (($puno > $pdos || $puno < $pdos) && ($puno > 45 || $pdos > 45)) {
        $puntuacion = 'Ventaja ' .$jugada;
        echo $puntuacion. ' </br>';
        continue;
    }
    //muestro los puntos de los competidores
    $puno == 0 ? $puntuacion .= 'Love -' .$pdos :
        ($pdos == 0 ? $puntuacion .= $puno. ' - Love' :
            (($puno != 0 && $pdos != 0) ? $puntuacion .= $puno. ' - ' .$pdos :
                null));
    echo $puntuacion. ' </br>';
}
