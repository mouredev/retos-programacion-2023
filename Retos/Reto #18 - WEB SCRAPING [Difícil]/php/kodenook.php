<?php

declare (strict_types = 1);

/**
 * The function scrapes a website and retrieves the text content of the blockquote elements, excluding
 * the first 21 elements.
 */
function scraping(): void
{
    $url = 'https://holamundo.day';

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);

    if ($response === false) {
        die('Error al realizar la solicitud');
    }

    $dom = new DOMDocument();
    libxml_use_internal_errors(true);
    $dom->loadHTML($response);
    libxml_clear_errors();

    $links = $dom->getElementsByTagName('blockquote');
    $i = 0;
    foreach ($links as $link) {
        if ($i < 21) {
            $i++;
            continue;
        }

        echo $link->textContent . PHP_EOL;
    }
}

scraping();
