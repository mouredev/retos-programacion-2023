<?php

declare(strict_types=1);

function removeChars(string $text): string 
{
    return preg_replace('/[^a-z]/', '', strtolower($text));
}

function isHeterogram(string $text): bool
{
    $newText = removeChars($text);

    $counts = count_chars($newText, 1);

    return max($counts) === 1;
}

function isIsogram(string $text): bool
{
    $newText = removeChars($text);

    $counts = count_chars($newText, 1);
    
    return max($counts) === min($counts);
}

function isPangram(string $text): bool
{
    $newText = removeChars($text);

    $counts = count_chars($newText, 3);
    
    return strlen($counts) === 26; 
}

echo 'Hectograma: '.isHeterogram('abcdef'). PHP_EOL;

echo 'Isograma: '. isIsogram('mama'). PHP_EOL;

echo 'Panagram: '. isPangram('The quick brown fox jumps over the lazy dog El veloz murcielagoñ hindu comia feliz cardillo y kiw Jackdaws love my big sphinx of quartz'). PHP_EOL;

?>