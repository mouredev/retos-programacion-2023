<?php

$points = ['Love', '15', '30', '40', 'Deuce', 'Ventaja'];

function setPoints(string $player, array $score)
{
	$score[$player] = $GLOBALS['points'][array_search($score[$player], $GLOBALS['points']) + 1];
	return $score;
}

function tennisMatch(array $pointsSequence)
{
	$score = [
		'P1' => 'Love',
		'P2' => 'Love',
	];
	
	foreach ($pointsSequence as $player) {
		$score = setPoints($player, $score);
		print($score['P1'] . ' - ' .$score['P2']). PHP_EOL;
	}
	
	echo end($pointsSequence) . " ha ganado el partido." . PHP_EOL;
}

tennisMatch(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);
