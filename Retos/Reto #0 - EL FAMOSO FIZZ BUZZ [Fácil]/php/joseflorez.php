<?php

$from = 1;
$to = 100;

function isMultiplo($from, $to)
{
	$result = array();

	for($i = $from; $i <= $to; $i++){
		$result[$i] = $i;
		
		if( ($i % 3) == 0 && ($i % 5) == 0 ) $result[$i] = 'FIZZBUZZ';
		else if( ($i % 3) == 0) $result[$i] = 'FIZZ';
		else if( ($i % 5) == 0) $result[$i] =  'BUZZ';
		
	}
	return $result;
}

function printResult($result)
{
	foreach ($result as $value) {
		print $value ."\n";
	}
}

$result = isMultiplo($from, $to);
printResult($result);