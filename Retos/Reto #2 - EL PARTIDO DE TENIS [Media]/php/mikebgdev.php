<?php

    enum Players:string 
    {
        case Player1 = 'Jugador 1';
        case Player2 = 'Jugador 2';
    }

    function tenisGame(array $playersPoints): void
    {
        $pointText = ['Love', '15', '30', '40'];
        $player1Points = 0;
        $player2Points = 0;

        foreach ($playersPoints as $player){
            if ($player == Players::Player1) $player1Points++;
            if ($player == Players::Player2) $player2Points++;



            if($player1Points >= 3 && $player2Points >=3){
                if ($player1Points === $player2Points) {
                    echo "Deuce\n";
                } else {
                    $ventaja = ($player1Points > $player2Points) ? Players::Player1->value : Players::Player2->value;
                    echo "Ventaja $ventaja\n";
                }

            } else {
                echo $pointText[$player1Points] . " - " . $pointText[$player2Points] ."\n";
            }

            
            if($player1Points >= 4 || $player2Points >=4){
                $ganador = ($player1Points > $player2Points) ? Players::Player1->value : Players::Player2->value;
                echo "Ha ganado: $ganador\n";
                return;
            }
        }
        
    }


    tenisGame(
        [
            Players::Player1,
            Players::Player1,
            Players::Player2,
            Players::Player2,
            Players::Player1,
            Players::Player2,
            Players::Player1,
            Players::Player1,
            Players::Player1,
        ]
    );

?>