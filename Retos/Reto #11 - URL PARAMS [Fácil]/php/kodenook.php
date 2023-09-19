<?php

declare(strict_types=1);


/**
 * The function `urlParams` takes a URL as input and returns an array of key-value pairs representing
 * the query parameters in the URL.
 * 
 * @param string url The parameter "url" is a string that represents a URL with query parameters.
 * 
 * @return array an array of URL parameters.
 */
function urlParams(string $url): array
{
    $query = explode('?', $url);
    $query = explode('&', $query[1]);

    foreach ($query as $value) {
        $params = explode('=', $value);

        $result[$params[0]] = $params[1];
    }

    return $result;
}

$params = urlParams('https://retosdeprogramacion.com?year=2023&challenge=0');

foreach ($params as $key => $value) {
    echo sprintf('%s = %s', $key, $value), PHP_EOL;
}
