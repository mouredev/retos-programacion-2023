<?php

    const LAGARTO = "🦎";
    const PIEDRA = "🗿";
    const PAPEL = "📄";
    const TIJERAS = "✂️";
    const SPOCK = "🖖";

    const GANA_CONTRA = array(
        PIEDRA => array(TIJERAS, LAGARTO),
        PAPEL => array(PIEDRA, SPOCK),
        TIJERAS => array(PAPEL, LAGARTO),
        LAGARTO => array(PAPEL, SPOCK),
        SPOCK => array(TIJERAS, PIEDRA)
    );

    function determinarJugadaGanadora($jugada1, $jugada2) 
    {
        if ($jugada1 == $jugada2) {
            return 0;
        } elseif (in_array($jugada2, GANA_CONTRA[$jugada1])) {
            return 1;
        } else {
            return 2;
        }
    }

    function piedraPapelTijeraLagartoSpock (array $jugadas)
    {
        $jugador1 = 0;
        $jugador2 = 0;

        foreach ($jugadas as $jugada) {
            $ganador = determinarJugadaGanadora($jugada[0], $jugada[1]);

            switch($ganador) {
                case 1:
                    $jugador1++;
                    break;
                case 2:
                    $jugador2++;
                    break;
                default:
                    break;
            }
        }

        if($jugador1 > $jugador2) {
            echo "Resultado: Ganador Jugador 1\n";
        } elseif ($jugador1 < $jugador2) {
            echo "Resultado: Ganador Jugador 2\n";
        } else {
            echo "Resultado: Empate\n";
        }

    }

    $pruebas = array(
        array(TIJERAS, PAPEL),
        array(PIEDRA, PAPEL),
        array(SPOCK, SPOCK),
        array(PIEDRA, PAPEL),
        array(SPOCK, PAPEL),
        array(LAGARTO, LAGARTO),
        array(SPOCK, LAGARTO),
    );

    $pruebas2 = array(
        array(TIJERAS, TIJERAS)
    );

    $pruebas3 = array(
        array(PIEDRA, TIJERAS),
        array(LAGARTO, SPOCK),
        array(SPOCK, LAGARTO),
    );

    piedraPapelTijeraLagartoSpock($pruebas);
    piedraPapelTijeraLagartoSpock($pruebas2);
    piedraPapelTijeraLagartoSpock($pruebas3);
?>