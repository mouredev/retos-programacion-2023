<?php

$plays = [["🗿","✂️"], ["✂️","🗿"], ["📄","🗿"], ["✂️","🗿"], ["✂️","🗿"]];

function whoWins($plays) {

    $p1Score = 0;
    $p2Score = 0;

    foreach ($plays as $play) {

        switch ($play[0]) {
            case '🗿':
                if ($play[1] == '✂️' || $play[1] == '🦎') {
                    $p1Score++;
                } elseif ($play[1] == '📄' || $play[1] == '🖖') {
                    $p2Score++;
                }
            break;
            case '📄':
                if ($play[1] == '🗿' || $play[1] == '🦎') {
                    $p1Score++;
                } elseif ($play[1] == '✂️' || $play[1] == '🖖') {
                    $p2Score++;
                }
            break;
            case '✂️':
                if ($play[1] == '📄' || $play[1] == '🖖') {
                    $p1Score++;
                } elseif ($play[1] == '🗿' || $play[1] == '🦎') {
                    $p2Score++;
                }
            break;
            case '🦎':
                if ($play[1] == '🖖' || $play[1] == '✂️') {
                    $p1Score++;
                } elseif ($play[1] == '🗿' || $play[1] == '📄') {
                    $p2Score++;
                }
            break;
            case '🖖':
                if ($play[1] == '🗿' || $play[1] == '✂️') {
                    $p1Score++;
                } elseif ($play[1] == '📄' || $play[1] == '🦎') {
                    $p2Score++;
                }
            break;
        }

    }

    if ($p1Score > $p2Score) {
        return "Player 1";
    } elseif ($p2Score > $p1Score) {
        return "Player 2";
    } else {
        return "Tie";
    }
}

echo whoWins($plays);

?>