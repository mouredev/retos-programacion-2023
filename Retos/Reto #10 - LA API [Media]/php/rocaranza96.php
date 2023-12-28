<?php

function request(string $url): string|bool
{
    return file_get_contents($url, false, stream_context_create([
        'http' => [
            'method' => 'GET',
            'header' => 'Content-type: application/json',
        ],
    ]));
}

$url = 'https://api.jikan.moe/v4/random/anime';
echo request($url);
