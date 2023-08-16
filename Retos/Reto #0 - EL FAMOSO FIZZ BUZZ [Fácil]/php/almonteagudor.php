<?php

for ($i = 1; $i <= 100; $i++)
{
    $fizzbuzzToPrint = $i % 3 == 0 ? 'fizz' : '';
    $fizzbuzzToPrint .= $i % 5 == 0 ? 'buzz' : '';

    $fizzbuzzToPrint = $fizzbuzzToPrint == '' ? $i : $fizzbuzzToPrint;

    echo($fizzbuzzToPrint . "\n");
}