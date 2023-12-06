<?php

declare(strict_types=1);

function requestApi(string $url): string
{
    $options = array(
        "http" => array(
            'method' => 'GET',
            'header' => 'Content-type: application/json'
        )
    );

    $context = stream_context_create($options);
    
    return file_get_contents($url, false, $context);
}


$url = 'https://api.waifu.im/tags';
echo requestApi($url) . PHP_EOL;

?>