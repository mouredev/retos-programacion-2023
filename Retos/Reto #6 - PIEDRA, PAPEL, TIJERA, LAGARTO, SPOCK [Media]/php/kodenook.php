<?php

declare(strict_types=1);

/**
 * The function `winnerPPTLS` determines the winner of a series of rock-paper-scissors-lizard-spock
 * games based on the given rules.
 * 
 * @param array games The parameter `games` is an array of arrays. Each inner array represents a game
 * and contains two elements. The first element represents the move of Player 1, and the second element
 * represents the move of Player 2. The moves can be one of the following emojis: "🗿"
 * 
 * @return string a string indicating the winner of the game. It can return "Tie" if both players have
 * the same number of wins, "Player 1" if player 1 has more wins, or "Player 2" if player 2 has more
 * wins.
 */
function winnerPPTLS(array $games): string
{
    $rules = [
        "🗿" => ["✂️", "🦎"],
        "📄" => ["🗿", "🖖"],
        "✂️" => ["📄", "🦎"],
        "🦎" => ["📄", "🖖"],
        "🖖" => ["🗿", "✂️"]
    ];

    $p1 = 0;
    $p2 = 0;


    foreach ($games as $game) {
        if ($game[0] !== $game[1]) {
            if (in_array($game[1], $rules[$game[0]])) $p1++;
            else $p2++;
        }
    }

    if ($p1 === $p2) return 'Tie' . PHP_EOL;
    elseif ($p1 > $p2) return 'Player 1' . PHP_EOL;
    else return 'Player 2' . PHP_EOL;
}

echo winnerPPTLS([["✂️", "✂️"]]);
echo winnerPPTLS([["✂️", "📄"]]);
echo winnerPPTLS([["🖖", "📄"]]);
echo winnerPPTLS([["🖖", "🗿"]]);
echo winnerPPTLS([["🖖", "🗿"], ["✂️", "🗿"], ["📄", "✂️"]]);
