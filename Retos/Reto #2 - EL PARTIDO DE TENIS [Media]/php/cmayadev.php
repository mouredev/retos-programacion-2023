<?php

$p1_score = 0;
$p2_score = 0;
$points_table = ["Love", 15, 30, 40];
$points = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];

foreach ($points as $point) {
    
    $point == "P1" && $p1_score++;
    $point == "P2" && $p2_score++;

    if ($p1_score <= 3 && $p2_score <= 3) {
        if ($p1_score == 3 && $p2_score == 3) {
            echo "Deuce\n";
        } else {
            echo $points_table[$p1_score] . ' - ' . $points_table[$p2_score] . "\n";
        }
    } else {
        if ($p1_score == $p2_score) {
            echo "Deuce\n";
        } elseif (abs($p1_score - $p2_score) == 1) {
            echo "Ventaja " . ($p1_score > $p2_score ? "P1\n" : "P2\n");
        } elseif (abs($p1_score - $p2_score) >= 2) {
            echo "Ha ganado el " . ($p1_score > $p2_score ? "P1\n" : "P2\n");
            break;
        }
    }

}

?>