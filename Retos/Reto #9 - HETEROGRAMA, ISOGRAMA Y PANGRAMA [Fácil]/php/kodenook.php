<?php

declare(strict_types=1);

/**
 * The function "isHeterogram" checks if a given string is a heterogram, meaning it contains only
 * unique letters.
 * 
 * @param string text The parameter "text" is a string that represents the input text that we want to
 * check if it is a heterogram.
 * 
 * @return bool a boolean value. It returns true if the input string is a heterogram (i.e., it contains
 * only unique letters) and false otherwise.
 */
function isHeterogram(string $text): bool
{
    if (ctype_alpha($text)) {
        $original = str_split($text);
        $filter = array_unique($original);

        if ($original === $filter) return true;
    }

    return false;
}

/**
 * The function checks if a given string is an isogram, meaning it does not contain any repeated
 * letters.
 * 
 * @param string text The input string that we want to check if it is an isogram.
 * 
 * @return bool a boolean value. It returns true if the input string is an isogram (i.e., it does not
 * contain any repeating letters) and false otherwise.
 */
function isIsogram(string $text): bool
{
    $original = str_split($text);
    $filter = array_unique($original);

    if ($original === $filter) return true;

    return false;
}

/**
 * The function checks if a given string is a pangram, meaning it contains all the letters of the
 * alphabet.
 * 
 * @param string text The parameter "text" is a string that represents the input text that we want to
 * check if it is a pangram.
 * 
 * @return bool a boolean value, either true or false.
 */
function isPangram(string $text): bool
{
    $letters = range('a', 'z');
    $filter = array_unique(str_split(strtolower($text)));

    foreach ($letters as $value) {
        if (array_search($value, $filter) === false) return false;
    }

    return true;
}

echo isHeterogram('jumpy'), PHP_EOL;
echo isHeterogram('jumpyyy'), PHP_EOL;
echo isIsogram('Background'), PHP_EOL;
echo isIsogram('Backgroundd'), PHP_EOL;
echo isPangram('The quick brown fox jumps over a lazy dog.'), PHP_EOL;
echo isPangram('The quick brown fox jumps over  lzy dog'), PHP_EOL;
