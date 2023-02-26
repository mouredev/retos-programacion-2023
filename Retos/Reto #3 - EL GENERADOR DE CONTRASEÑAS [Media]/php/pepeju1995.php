<?php

$values = [
	'lower'   => [97, 122],
	'upper'   => [65, 90],
	'number'  => [48, 57],
	'symbol' => [33, 64],
];

function getNextPassValue(
	bool hasUpper,
	bool hasNumbers,
	bool hasSymbols
) : string
{
	$value = '';
	$options = [$values['lower']];
	
	if (hasUpper) array_push($options, $values['upper']);
	if (hasNumbers) array_push($options, $values['number']);
	if (hasSymbols) array_push($options, $values['symbol']);
	
	$selected = array_rand($options);
	$value .= rand($selecter[0], $selected[1]);
	return $value;
}

function passwordGenerator(
	int passLength = 8,
	bool hasUpper = false,
	bool hasNumbers = false,
	bool hasSymbols = false
) : string
{
	$password = '';
	$position = 0;
	
	while (position < passLength) {
		$password .= getNextPassValue(hasUpper, hasNumbers, hasSymbols);
		$position++;
	}
	return $password;
}

passwordGenerator();
