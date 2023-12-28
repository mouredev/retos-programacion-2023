<?php

function checkHeterograma(string $text): bool
{
    $text = mb_strtolower($text);
    $letters = mb_str_split($text);
    $lettersCounted = array_count_values($letters);

    return count($letters) === count($lettersCounted);
}

function checkIsograma(string $text): bool
{
    $text = mb_strtolower($text);
    $letters = mb_str_split($text);
    $lettersCounted = array_count_values($letters);
    $uniqueLettersCounted = array_unique($lettersCounted);

    return count($uniqueLettersCounted) === 1;
}

function checkPangrama(string $text): bool
{
    $text = mb_strtolower($text);
    $alphabet = array_merge(range("a", "z"), ["á", "é", "í", "ó", "ú", "ü", "ñ"]);
    $unusedLetters = array_diff($alphabet, mb_str_split($text));

    return !count($unusedLetters);
}

$text = "Alberto";

echo("$text" . (checkHeterograma($text) ? "" : " no") . " es un heterograma\n");
echo("$text" . (checkIsograma($text) ? "" : " no") . " es un isograma\n");
echo("$text" . (checkPangrama($text) ? "" : " no") . " es un pangrama\n");

$text = "almonteagudor";

echo("$text" . (checkHeterograma($text) ? "" : " no") . " es un heterograma\n");
echo("$text" . (checkIsograma($text) ? "" : " no") . " es un isograma\n");
echo("$text" . (checkPangrama($text) ? "" : " no") . " es un pangrama\n");

$text = implode(array_merge(range("a", "z"), ["á", "é", "í", "ó", "ú", "ü", "ñ"]));

echo("$text" . (checkHeterograma($text) ? "" : " no") . " es un heterograma\n");
echo("$text" . (checkIsograma($text) ? "" : " no") . " es un isograma\n");
echo("$text" . (checkPangrama($text) ? "" : " no") . " es un pangrama\n");

$text = implode(array_merge(range("a", "z"), ["á", "é", "í", "ó", "ú", "ü", "ñ"], range("a", "z"), ["á", "é", "í", "ó", "ú", "ü", "ñ"]));

echo("$text" . (checkHeterograma($text) ? "" : " no") . " es un heterograma\n");
echo("$text" . (checkIsograma($text) ? "" : " no") . " es un isograma\n");
echo("$text" . (checkPangrama($text) ? "" : " no") . " es un pangrama\n");

$text = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja.";

echo("$text" . (checkHeterograma($text) ? "" : " no") . " es un heterograma\n");
echo("$text" . (checkIsograma($text) ? "" : " no") . " es un isograma\n");
echo("$text" . (checkPangrama($text) ? "" : " no") . " es un pangrama\n");


