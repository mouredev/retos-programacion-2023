<?php

$fizz = 3;
$buzz = 5;
for($i=1;$i<=100;$i++) {
    $fizzbuzz = $i;
    if (!($i % $fizz)) {
        $fizzbuzz = 'fizz';
    }
    if (!($i % $buzz)) {
        $fizzbuzz = 'buzz';
    }
    if (!($i % ($fizz*$buzz))) {
        $fizzbuzz = 'fizzbuzz';
    }
    printf("%s (%d)\n", $fizzbuzz, $i);
}
