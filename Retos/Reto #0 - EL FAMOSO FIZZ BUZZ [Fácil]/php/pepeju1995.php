<?php

for ($i = 1; $i <= 100; $i++) {
	$fizz = $i % 3 === 0;
	$buzz = $i % 5 === 0;
	$newLine = "";

	echo ($fizz && $buzz ? 'fizzbuzz' : ($fizz ? 'fizz' : ($buzz ? 'buzz' : $i))) . "\n";
}
