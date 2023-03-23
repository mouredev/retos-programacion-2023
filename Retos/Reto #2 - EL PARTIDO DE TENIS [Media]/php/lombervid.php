<?php

function getScore(int $p1, int $p2, bool &$ended = false): string
{
    $scoreTerms = ['Love', '15', '30', '40'];
    $p1Score = $scoreTerms[$p1] ?? '';
    $p2Score = $scoreTerms[$p2] ?? '';

    if ($ended) {
        throw new Exception("Game had already ended. Invalid extra scores.", 1);
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
    $ended = false;
    $matchScores = [];

    foreach ($scores as $i => $score) {
        $matchScores[] = match (strtoupper($score)) {
            'P1' => getScore(++$p1, $p2, $ended),
            'P2' => getScore($p1, ++$p2, $ended),
            default => throw new Exception("Invalid score: \"{$score}\" at position {$i}", 1),
        };
    }

    if (!$ended) {
        throw new Exception("Not enough scores to finish the match.", 1);
    }

    return $matchScores;
}

// Main Code
$matches = [
    ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P3', 'P1'],
    ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1', 'P2'],
    ['P1', 'P1', 'P2'],
    ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'],
    ['P1', 'P1', 'P1', 'P1'],
];

foreach ($matches as $index => $match) {
    try {
        $match = getMatchScore($match);

        echo "Match {$index} Result:\n";

        foreach ($match as $score) {
            echo "{$score}\n";
        }
    } catch (\Throwable $th) {
        echo "Match {$index} has been skipped with the error: {$th->getMessage()}\n";
    }
    echo "\n";
}
