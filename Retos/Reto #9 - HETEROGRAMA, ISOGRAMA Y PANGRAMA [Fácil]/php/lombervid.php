<?php

declare(strict_types=1);

function clearString(string $str): string
{
    return preg_replace('/[^a-z]+/', '', strtolower($str));
}

function isIsogram(string $phrase): bool
{
    $str = clearString($phrase);

    if (!$str) {
        return false;
    }

    $counts = count_chars($str, 1);

    return max($counts) === min($counts);
}

function isHeterogram(string $phrase): bool
{
    $str = clearString($phrase);

    if (!$str) {
        return false;
    }

    $counts = count_chars($str, 1);

    return max($counts) === 1;
}

function isPangram(string $phrase): bool
{
    $str = clearString($phrase);

    if (!$str) {
        return false;
    }

    $characters = count_chars($str, 3);

    return $characters === implode('', range('a', 'z'));
}
