<?php

function TennisMatch($list){
    $p1Points = 0;
    $p2Points = 0;

    foreach($list as $item){
        switch(strtoupper($item)){
            case "P1":
                $p1Points++;
                break;
            case "P2":
                $p2Points++;
                break;
            default:
                echo "Error en el tanteo";
                return;
        }

        if ($p1Points == 4 && $p2Points == 4 ){
            $p1Points = 3;
            $p2Points = 3;
        }

        PrintScore($p1Points, $p2Points);
    }
}

function PrintScore ($P1, $P2){
    
    $score = ["Love", "15", "30", "40"];

    if ($P1 == 3 && $P2 == 3){
        echo "\tDeuce\n";
    }
    else if ($P1 == 4 && $P2 == 3) {
        echo "\tVentaja P1\n";
    }
    else if ($P2 == 4 && $P1 == 3) {
        echo "\tVentaja P2\n";
    }
    else if ($P1 == 5 && ($P1 - $P2) == 2) {
        echo "\tGana P1\n";
    }
    else if ($P2 == 5 && ($P2 - $P1) == 2) {
        echo "\tGana P2\n";
    }
    else {
        echo "P1:\t" . $score[$P1] . " - " . $score[$P2]. "\t:P2\n";
    }
}

TennisMatch(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]);
TennisMatch(["P1", "P1", "P1", "P2", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"])
?>