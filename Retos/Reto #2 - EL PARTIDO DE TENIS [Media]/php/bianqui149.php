<?php
/* A class that contains the logic of the tennis game. */
class TennisMatch
{
    private const Points = [
        'Love',
        '15',
        '30',
        '40',
    ];
    public $pointFromMatch;

    public function __construct(array $pointFromMatch)
    {
        $this->pointFromMatch = $pointFromMatch;
    }

    /**
     * The function takes an array of strings as input and returns an array of strings as output
     * 
     * @return array the score of the match.
     */
    public function MatchStarted()
    {
        $secuency     = $this->pointFromMatch;
        $score        = [];
        $isPlayerOne  = 0;
        $isPlayerTwo  = 0;
        foreach ($secuency as $key => $player_point) {
            $p1 = ('P1' === $player_point) ? $isPlayerOne++ + 1 : $isPlayerOne;
            $p2 = ('P2' === $player_point) ? $isPlayerTwo++ + 1 : $isPlayerTwo;
            if ($p1 === 4 && ($p1 - $p2) >= 2) {
                $score[] = 'Ha Ganado P1';
                break;
            }
            if ($p2 === 4 && ($p2 - $p1) >= 2) {
                $score[] = 'Ha Ganado P2';
                break;
            } else {
                $score[] = $this->FormatStringValues($p1, $p2);
            }
        }
        return $score;
    }
    /**
     * It takes two integers as parameters, and returns a string
     * 
     * @param int pl1 Player 1's score
     * @param int pl2 The score of player 2
     * 
     * @return string the current status of the match.
     */
    public function FormatStringValues(int $pl1, int $pl2)
    {
        $value_score_user_one = ($pl1 < 4) ? self::Points[$pl1] : $pl1;
        $value_score_user_two = ($pl2 < 4) ? self::Points[$pl2] : $pl2;
        $string               = $value_score_user_one .  ' - ' . $value_score_user_two;
        if ($value_score_user_one === $value_score_user_two && $value_score_user_two === '40') {
            $string = 'Deuce';
        }
        if ($pl1 === 4 && $pl2 !== 4) {
            $string = 'Ventaja P1';
        }
        if ($pl1 !== 4 && $pl2 === 4) {
            $string = 'Ventaja P2';
        }
        if ($pl1 === 5 && $pl2 !== 5) {
            $string = 'Ha Ganado P1';
        }
        if ($pl1 !== 5 && $pl2 === 5) {
            $string = 'Ha Ganado P2';
        }
        return $string;
    }


    public function __toString()
    {
        $match = $this->MatchStarted();
        $match_end = implode("\n", $match);
        return $match_end;
    }
}

$match1 = new TennisMatch(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);
//$match2 = new TennisMatch(['P1', 'P1', 'P1', 'P2', 'P1']);
//$match3 = new TennisMatch(['P1', 'P1', 'P1', 'P1']);
echo $match1;
