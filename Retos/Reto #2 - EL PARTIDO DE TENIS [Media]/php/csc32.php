<?php 
/*  solution based in @lombervid solution because always I get tanglep up after receive the players plays  
*/

function tenisScore(int $playP1, int $playP2 ): string{
    global $gamePoints;
    $points = ['love', '15', '30','40'];
    static $matchEnds = false;
    $playerPoints1 = $points[$playP1] ?? "";
    $playerPoints2 = $points[$playP2] ?? "";

    $gamePoints = "";
    if ($matchEnds) {
        exit("The match has ended \n");
    }

    if ($playP1 < 3 && $playP2 < 3) {
        $gamePoints = "$playerPoints1 - $playerPoints2";
        return $gamePoints;
    }

    if ($playP1 == 3 && $playP2 == 3) {
        $gamePoints = "Deuce";
        return $gamePoints;
    }

    if ($playP1 > $playP2) {
        if($playP1 - $playP2 > 1){
        $gamePoints = "Player 1 has win \n";
        print $gamePoints;
        $matchEnds = true;
        return $gamePoints;
        }
        $gamePoints = $playerPoints1 ? "$playerPoints1 - $playerPoints2" : "Advantage player 1";

        return $gamePoints;
    }
    if ($playP2 - $playP1 > 1) {
        $gamePoints = "Player 2 has win \n";
        print $gamePoints;
        $matchEnds = true;
        return $gamePoints;
    }
    $gamePoints = $playerPoints2 ? "$playerPoints1 - $playerPoints2" : "advantage player 2";

    if ($playP2 > $playP1) {
    $gamePoints =  "advantage player 2";
    return $gamePoints;
    }

    return $gamePoints;
}
function getTenisPlau(Array $seqPlayer = []) : Array{
    $playP1 = 0;
    $playP2 = 0;
    $matchPoints = [];
    foreach ($seqPlayer as $i => $playerPoint){
        array_push( $matchPoints ,match (strtoupper($playerPoint)){
            'P1' => tenisScore(++$playP1,$playP2),
            'P2' => tenisScore($playP1, ++$playP2),
            default => throw new Exception("Invalid Player " . " {$playerPoint} " . "at position {$i} \n" ),   
        });
    }
    return $matchPoints;
}
try {
    
$playsGame = ['P1', 'P1', 'P1', 'P2', 'P1', 'P2', 'P1', 'P1'];
print "P1 - P2 \n";
foreach(getTenisPlau($playsGame) as $point){
    print $point . "\n";
};
} catch (Exception $e) {
    print $e->getMessage() . "\n";
}
?>