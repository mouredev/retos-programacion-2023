<?php

function getScore(int $p1, int $p2): string
{
    static $ended = false;
    $scoreTerms = ['Love', '15', '30', '40'];
    $p1Score = $scoreTerms[$p1] ?? '';
    $p2Score = $scoreTerms[$p2] ?? '';

    if ($ended) {
        exit("Game had already ended. Invalid extra scores.\n");
    }

    if ($p1 === $p2 && $p1 >= 3) {
        return 'Deuce';
    }

    if ($p1 <= 3 && $p2 <= 3) {
        return "{$p1Score} - {$p2Score}";
    }

    if ($p1 > $p2) {
        if ($p1 - $p2 > 1) {
            $ended = true;
            return 'Ha ganado P1';
        }

        return 'Ventaja P1';
    }

    if ($p2 - $p1 > 1) {
        $ended = true;
        return 'Ha ganado P2';
    }

    return 'Ventaja P2';
}

function getMatchScore(array $scores): array
{
    $p1 = 0;
    $p2 = 0;
    $matchScores = [];

    foreach ($scores as $i => $score) {
        $matchScores[] = match (strtoupper($score)) {
            'P1' => getScore(++$p1, $p2),
            'P2' => getScore($p1, ++$p2),
            default => exit("Invalid score: \"{$score}\" at position {$i}\n"),
        };
    }

    return $matchScores;
}

// Main Code
$scores = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'];

foreach (getMatchScore($scores) as $score) {
    echo "{$score}\n";
}
