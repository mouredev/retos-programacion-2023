<?php

declare (strict_types = 1);

/**
 * The `stats` function takes a string as input and returns a string containing various statistics
 * about the input text, including the word count, the largest word, the sentence count, and the
 * average number of letters per word.
 *
 * @param string txt The parameter `txt` is a string that represents a text.
 *
 * @return string a string that contains the following information:
 */
function stats(string $txt): string
{
    $txt = explode(' ', $txt);
    $largest = '';
    $sentences = 0;
    $letter_counts = [];

    foreach ($txt as $value) {
        if (count(str_split($value)) > count(str_split($largest))) {
            $largest = $value;
        }
        if (str_ends_with($value, '.')) {
            $sentences++;
        }
        $value = str_replace('.', '', $value); // Corregir aquí
        array_push($letter_counts, count(str_split($value)));
    }

    $response = 'Words count: ' . count($txt) . PHP_EOL;
    $response .= 'Largest word: ' . $largest . PHP_EOL;
    $response .= 'Sentences count: ' . $sentences . PHP_EOL;
    $response .= 'Average letter: ' . array_sum($letter_counts) / count($letter_counts) . PHP_EOL;

    return $response;
}

$sentence = 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Minus laudantium numquam quam ex velit consequatur in repellendus praesentium ab? Esse dolor voluptates recusandae at, odit necessitatibus provident sint placeat. Recusandae.';
echo stats($sentence);
